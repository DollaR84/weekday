from datetime import datetime, timedelta
from itertools import cycle

import wx

from ..player import Player

from ..utils import Interval, types


class Signal:

    def __init__(self):
        self.time_period: timedelta = timedelta(seconds=0)

        self.time_interval_generator = self._time_interval_generator()

        self.track_process = None
        self.set_signal()

    def _time_interval_generator(self) -> int:
        for minutes in cycle([60, 30, 15, 0]):
            yield minutes

    def set_time_period(self, value: int):
        minutes_current_value = value * 60
        self.time_period = timedelta(seconds=minutes_current_value)

    def next_time_interval(self) -> str:
        time_period = next(self.time_interval_generator)
        self.set_time_period(time_period)
        return Interval.to_str(self.time_period, types.TimeUnit.MINUTES)

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
            self.track_process = wx.CallLater(time_period.total_seconds() * 1000, self.signal)

    def signal(self):
        Player.play(2)
        self.track_process = wx.CallLater(self.time_period.total_seconds() * 1000, self.signal)
