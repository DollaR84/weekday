import addonHandler

from .base import BaseAlarmAction, BaseTimerAction

from ..entities import Alarm


addonHandler.initTranslation()


class AlarmAction(BaseAlarmAction, BaseTimerAction):

    @property
    def name(self) -> str:
        return _("Alarm")

    def create(self):
        self.entity = Alarm()

    def press_2(self) -> str:
        if self.is_settings:
            time_period_str = self.entity.set_time_period()
            return "\n".join([_("Alarm time period set"), time_period_str])
        return super().press_2()
