from datetime import datetime

import addonHandler

import wx

from .base import BaseAlarm

from ..utils import Player, types


addonHandler.initTranslation()


class Alarm(BaseAlarm):

    def set_signal(self):
        if self.need_reminder:
            self.track_process = wx.CallLater(30 * 1000, self.signal)
        elif self.time_period:
            now = datetime.now()
            self.time_finished = now.replace(
                hour=round(self.hours_current_value // self.factor(types.TimeUnit.HOURS)),
                minute=round(self.minutes_current_value // self.factor(types.TimeUnit.MINUTES)),
                second=round(self.seconds_current_value // self.factor(types.TimeUnit.SECONDS)),
            )
            self.is_running = True
            self.need_reminder = True

            time_period = self.time_finished - datetime.now()
            self.track_process = wx.CallLater(int(time_period.total_seconds()) * 1000, self.signal)

    def start(self) -> str:
        bounce = 2 if self.time_unit == types.TimeUnit.HOURS else 10
        self.calc_time_period(bounce)
        self.set_signal()
        if self.track_process:
            return _("Alarm started")

    def stop(self) -> str:
        if self.track_process:
            self.track_process.Stop()
            self.track_process = None
        self._stop()
        return _("The alarm is disabled")

    def signal(self):
        Player.play(1)
        self.set_signal()

    def load_data(self, data: dict):
        super().load_data(data)
        self.set_signal()
