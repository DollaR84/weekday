﻿import addonHandler

from .base import BaseAction

from ..entities import Weekday


addonHandler.initTranslation()


class WeekdayAction(BaseAction):

    def __init__(self):
        super().__init__()

        self.weekday: Weekday = Weekday

    @property
    def name(self) -> str:
        return _("Weekday")

    @property
    def is_started(self) -> bool:
        return True

    @property
    def is_settings(self) -> bool:
        return False

    def additional(self) -> str:
        return self.press_1()

    def press_1(self) -> str:
        return self.weekday.get_week_day()
