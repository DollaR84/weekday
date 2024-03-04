from datetime import datetime

import addonHandler

import wx

from .base import BaseAlarm

from ..player import Player

from ..utils import types


addonHandler.initTranslation()


class Alarm(BaseAlarm):

    def start(self) -> str:
        bounce = 2 if self.time_unit == types.TimeUnit.HOURS else 10
        self.calc_time_period(bounce)
        if self.time_period:
            now = datetime.now()
            self.time_finished = now.replace(
                hour=round(self.hours_current_value // self.factor(types.TimeUnit.HOURS)),
                minute=round(self.minutes_current_value // self.factor(types.TimeUnit.MINUTES)),
                second=round(self.seconds_current_value // self.factor(types.TimeUnit.SECONDS)),
            )
            self.is_running = True

            time_period = self.time_finished - datetime.now()
            self.track_process = wx.CallLater(time_period.total_seconds() * 1000, self.check_stop_and_signal)
            return _("Alarm started")

    def stop(self) -> str:
        if self.track_process:
            self.track_process.Stop()
            self.track_process = None
        self._stop()
        return _("The alarm is disabled")

    def check_stop_and_signal(self):
        self._stop()
        Player.play(1)
