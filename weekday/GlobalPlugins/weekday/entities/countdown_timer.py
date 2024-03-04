from datetime import datetime

import addonHandler

import wx

from .base import BaseTimer, BaseAlarm

from ..player import Player

from ..utils import types


addonHandler.initTranslation()


class CountDownTimer(BaseTimer, BaseAlarm):

    def __init__(self):
        super().__init__()

        self.time_started: datetime | None = None

    def get(self):
        if self.resume_period:
            return _("countdown timer pause")

        return super().get()

    def start(self) -> str:
        bounce = 2 if self.time_unit == types.TimeUnit.HOURS else 10
        self.calc_time_period(bounce)
        if self.time_period:
            self.time_started = datetime.now()
            self.time_finished = self.time_started + self.time_period
            self.is_running = True

            self.track_process = wx.CallLater(self.time_period.total_seconds() * 1000, self.check_stop_and_signal)
            return _("Countdown timer started")

    def stop(self) -> str:
        if self.track_process:
            self.track_process.Stop()
            self.track_process = None
        self._stop()
        return _("The countdown timer is disabled")

    def _stop(self):
        self.time_started = None
        super()._stop()

    def pause(self) -> str:
        self.resume_period = datetime.now() - self.time_started
        return _("countdown timer pause")

    def resume(self) -> str:
        if datetime.now() >= self.time_finished:
            return self.stop()

        self.resume_period = None
        return _("countdown timer resume")

    def check_stop_and_signal(self):
        self._stop()
        Player.play(0)
