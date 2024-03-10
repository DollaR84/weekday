import addonHandler

from .base import BaseAlarmAction, BaseTimerAction

from ..entities import CountDownTimer


addonHandler.initTranslation()


class CountDownTimerAction(BaseTimerAction, BaseAlarmAction):

    @property
    def name(self) -> str:
        return _("Countdown timer")

    def create(self):
        self.entity = CountDownTimer()

    def press_2(self) -> str:
        if self.is_settings:
            time_period_str = self.entity.set_time_period()
            return "\n".join([_("Countdown timer time period set"), time_period_str])
        return super().press_2()
