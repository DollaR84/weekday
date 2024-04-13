import addonHandler
import wx

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

    def additional(self) -> str:
        return self.entity.change_type()

    def additional2(self, press_count: int):
        match press_count:
            case 1:
                return wx.CallAfter(self.entity.run_fast_open_program)
            case 2:
                wx.CallAfter(self.entity.select_fast_open_program)

    def press_1(self) -> str:
        if not self.entity:
            self.create()

        return self.entity.get_week_day()

    def press_2(self) -> str:
        return self.entity.get_text()
