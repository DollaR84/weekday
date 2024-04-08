from datetime import datetime, timedelta
from itertools import cycle

import addonHandler
import ui
import wx

from .base import BaseEntity

from ..utils import Interval, Player, types


addonHandler.initTranslation()


class Signal(BaseEntity):

    def __init__(self):
        self.time_period: timedelta = timedelta(seconds=0)
        self.type: types.SignalType = types.SignalType.SOUND

        self.time_interval_generator = self._time_interval_generator()
        self.signal_type_generator = self._signal_type_generator()

        self.track_process = None
        self.set_signal()

    def _time_interval_generator(self) -> int:
        for minutes in cycle([60, 30, 15, 0]):
            yield minutes

    def _signal_type_generator(self) -> int:
        for type_ in cycle(types.SignalType):
            yield type_

    def set_time_period(self, value: int):
        minutes_current_value = value * 60
        self.time_period = timedelta(seconds=minutes_current_value)

    def next_time_interval(self) -> str:
        time_period = next(self.time_interval_generator)
        self.set_time_period(time_period)
        return Interval.to_str(self.time_period, types.TimeUnit.MINUTES)

    def change_type(self) -> str:
        type_ = next(self.signal_type_generator)
        self.type = type_

        match type_:
          case types.SignalType.SOUND:
              return _("signal type sound")
          case types.SignalType.SPEECH:
              return _("signal type speech")
          case types.SignalType.SOUND_AND_SPEECH:
              return _("signal type sound and speech")
          case types.SignalType.OFF:
              return _("signal type off")

    def get(self):
        text = self.next_time_interval()
        self.set_signal()
        return text

    def set_signal(self):
        minutes = round(self.time_period.total_seconds() // 60)
        if minutes == 0:
            if self.track_process:
                self.track_process.Stop()
            self.track_process = None
        else:
            now = datetime.now()
            minutes_to_add = (-(now.minute % minutes) + minutes) % minutes
            time_finished = now + timedelta(minutes=minutes_to_add)
            time_finished = time_finished.replace(second=0, microsecond=0)
            time_period = time_finished - now
            self.track_process = wx.CallLater(int(time_period.total_seconds()) * 1000, self.signal)

    def signal(self):
        if self.type != types.SignalType.OFF:
            if self.type in (types.SignalType.SPEECH, types.SignalType.SOUND_AND_SPEECH):
                now = datetime.now()
                minute = now.minute if (now.minute % 5) == 0 else now.minute + 1
                time_period = timedelta(hours=now.hour, minutes=minute)
                ui.message(Interval.to_str(time_period))
            if self.type in (types.SignalType.SOUND, types.SignalType.SOUND_AND_SPEECH):
                Player.play(2)
            self.track_process = wx.CallLater(int(self.time_period.total_seconds()) * 1000, self.signal)

    def save_data(self) -> dict:
        data = super().save_data()
        data.update(time_period=self.time_period, type=self.type)
        return data

    def load_data(self, data: dict):
        super().load_data(data)
        self.set_signal()
