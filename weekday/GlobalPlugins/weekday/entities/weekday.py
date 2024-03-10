from datetime import datetime

import addonHandler

from .base import BaseEntity


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
