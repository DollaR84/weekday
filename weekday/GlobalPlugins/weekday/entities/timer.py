from datetime import datetime

import addonHandler

from ..utils import Interval


addonHandler.initTranslation()


class Timer:

    def __init__(self):
        self.time_started = datetime.now()

    def get(self):
        now = datetime.now()
        return Interval.to_str(now - self.time_started)

    def start(self) -> str:
        return _("Timer started")

    def stop(self) -> str:
        last_time = self.get()
        return "\n".join([_("The timer is disabled. Working hours:"), last_time])
