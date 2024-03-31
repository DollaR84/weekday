from datetime import datetime
import json
import logging
import requests

import addonHandler
from languageHandler import getLanguage

from .base import BaseEntity

from ..utils import translate


addonHandler.initTranslation()


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
        self.translate_url = "https://translate.astian.org/translate"

        self.lang = getLanguage()
        self._holidays = {}

    def _request(self, url: str):
        try:
            response = requests.get(url)
        except Exception as error:
            logging.error(error, exc_info=True)
            response = None

        return response

    @property
    def holidays(self) -> dict:
        if not self._holidays:
            now = datetime.now()
            response = self._request("/".join([self.nager_api_url, str(now.year), "ua"]))
            public_holidays = json.loads(response.content) if response else []
            for holiday in public_holidays:
                self._holidays[holiday["date"]] = holiday["localName"]
        return self._holidays

    def get_date_fact(self, date: datetime):
        response = self._request("/".join([self.numbers_api_url, str(date.month), str(date.day), "date"]))
        date_fact = response.content.decode("utf-8") if response else ""
        if date_fact:
            date_fact = translate(date_fact, self.lang, "en")
        return date_fact

    def get_text(self):
        now = datetime.now()
        text = self.holidays.get(now.strftime("%Y-%m-%d"), "")
        date_fact = self.get_date_fact(now)

        text = "\n".join([text, date_fact])
        return text
