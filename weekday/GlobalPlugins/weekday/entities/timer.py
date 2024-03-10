from datetime import datetime

import addonHandler

from .base import BaseTimer

from ..utils import Interval


addonHandler.initTranslation()


class Timer(BaseTimer):

    def __init__(self):
        super().__init__()

        self.time_started = datetime.now()

    def get(self):
        if self.resume_period:
            return "\n".join([Interval.to_str(self.resume_period), _("timer pause")])
        else:
            now = datetime.now()
            return Interval.to_str(now - self.time_started)

    def start(self) -> str:
        return _("Timer started")

    def pause(self) -> str:
        self.resume_period = datetime.now() - self.time_started
        return _("timer pause")

    def resume(self) -> str:
        self.time_started = datetime.now() - self.resume_period
        self.resume_period = None
        return _("timer resume")

    def stop(self) -> str:
        if self.resume_period:
            last_time = Interval.to_str(self.resume_period)
        else:
            last_time = Interval.to_str(datetime.now() - self.time_started)
        return "\n".join([_("The timer is disabled. Working hours:"), last_time])

    def save_data(self) -> dict:
        data = super().save_data()
        data.update(time_started=self.time_started)
        return data
