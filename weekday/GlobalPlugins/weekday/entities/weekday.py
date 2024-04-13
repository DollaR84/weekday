from datetime import datetime
from itertools import cycle
import json
import logging
import os
import requests

import addonHandler
from languageHandler import getLanguage

from gui import mainFrame
from gui.message import displayDialogAsModal
import wx

from .base import BaseEntity

from ..utils import translate, types


addonHandler.initTranslation()


class WikiEvent:
    __slots__ = ("year", "description",)

    def __init__(self, year: int, description: str):
        self.year = year
        self.description = description


class Weekday(BaseEntity):

    days = [
        _("Monday"),
        _("Tuesday"),
        _("Wednesday"),
        _("Thursday"),
        _("Friday"),
        _("Saturday"),
        _("Sunday"),
    ]

    @classmethod
    def get_week_day(cls):
        now = datetime.now()
        num_day = datetime.weekday(now)
        if num_day >= len(cls.days):
            return _("Error")

        return cls.days[num_day]

    def __init__(self):
        self.nager_api_url = "https://date.nager.at/api/v3/publicholidays"
        self.numbers_api_url = "http://numbersapi.com"
        self.wiki_api_url = "https://byabbe.se/on-this-day"
        self.translate_url = "https://translate.astian.org/translate"

        self.current_day = 0
        self.lang = getLanguage()
        self._holidays = {}
        self._wiki_events = {}
        self.next_wiki_event_id = 0

        self.type: types.DateEventType = types.DateEventType.SOURCE1
        self.event_type_generator = self._event_type_generator()

        self.fast_open_program: str | None = None

    def _event_type_generator(self) -> types.DateEventType:
        for type_ in cycle(types.DateEventType):
            yield type_

    def change_type(self) -> str:
        type_ = next(self.event_type_generator)
        self.type = type_

        match type_:
          case types.DateEventType.SOURCE1:
              return _("date event source type 1")
          case types.DateEventType.SOURCE2:
              return _("date event source type 2")
          case types.DateEventType.SOURCE12:
              return _("date event source type 1 and 2")
          case types.DateEventType.DISABLED:
              return _("date event source type off")

    def _request(self, url: str):
        try:
            response = requests.get(url)
        except Exception as error:
            logging.error(error, exc_info=True)
            response = None

        return response

    @property
    def holidays(self) -> dict:
        now = datetime.now()
        if not self._holidays or self.current_day != now.day:
            self.current_day = now.day
            response = self._request("/".join([self.nager_api_url, str(now.year), "ua"]))
            public_holidays = json.loads(response.content) if response else []
            for holiday in public_holidays:
                self._holidays[holiday["date"]] = holiday["localName"]
        return self._holidays

    def get_date_fact(self):
        now = datetime.now()
        response = self._request("/".join([self.numbers_api_url, str(now.month), str(now.day), "date"]))
        date_fact = response.content.decode("utf-8") if response else ""
        if date_fact:
            date_fact = translate(date_fact, self.lang, "en")
        return date_fact

    @property
    def wiki_events(self):
        now = datetime.now()
        if not self._wiki_events or self.current_day != now.day:
            response = self._request(
                "/".join([
                    self.wiki_api_url, str(now.month), str(now.day), "events.json",
                ])
            )
            events = response.json() if response else {}

            for index, event in enumerate(events.get("events", []), 1):
                self._wiki_events[index] = WikiEvent(event.get("year"), event.get("description"))
                self.next_wiki_event_id = index
        return self._wiki_events

    def get_wiki_event(self):
        event_str = ""
        events = self.wiki_events
        if self.next_wiki_event_id > 0:
            event = events.get(self.next_wiki_event_id, "")
            now = datetime.now()
            event_str = " ".join([f"{now.day}.{now.month}.{event.year}", event.description])
            event_str = translate(event_str, self.lang, "en")
            self.next_wiki_event_id -= 1
        return event_str

    def get_text(self):
        now = datetime.now()
        text = self.holidays.get(now.strftime("%Y-%m-%d"), "")

        if self.type in (types.DateEventType.SOURCE2, types.DateEventType.SOURCE12,):
            event_str = self.get_wiki_event()
            text = "\n".join([text, event_str])

        if self.type in (types.DateEventType.SOURCE1, types.DateEventType.SOURCE12,):
            date_fact = self.get_date_fact()
            text = "\n".join([text, date_fact])

        return text

    def save_data(self) -> dict:
        data = super().save_data()
        data.update(type=self.type, fast_open_program=self.fast_open_program)
        return data

    def select_fast_open_program(self):
        message = _("Select a program to fast launch")
        wildcard = "Executable files (*.exe)|*.exe|Scripts files (*.bat; *.cmd)|*.bat;*.cmd"
        mainFrame.prePopup()
        file_dialog = wx.FileDialog(
            mainFrame,
            message=message,
            wildcard=wildcard,
            defaultDir="c:",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        )

        if displayDialogAsModal(file_dialog) == wx.ID_CANCEL:
            mainFrame.postPopup()
            return

        self.fast_open_program = file_dialog.GetPath()
        mainFrame.postPopup()

    def run_fast_open_program(self):
        if not self.fast_open_program:
            return self.select_fast_open_program()

        path = os.path.dirname(self.fast_open_program).replace("\\", "\\\\")
        fast_open_program = self.fast_open_program.replace("\\", "\\\\")

        os.chdir(path)
        os.startfile(fast_open_program)
