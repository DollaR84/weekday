import addonHandler

from .base import BaseAction

from ..entities import Weekday


addonHandler.initTranslation()


class WeekdayAction(BaseAction):

    def create(self):
        self.entity: Weekday = Weekday()

    @property
    def name(self) -> str:
        return _("Weekday")

    @property
    def is_started(self) -> bool:
        return True

    @property
    def is_settings(self) -> bool:
        return False

    def press_1(self) -> str:
        if not self.entity:
            self.create()

        return self.entity.get_week_day()

    def press_2(self) -> str:
        return self.entity.get_text()
