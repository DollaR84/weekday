import addonHandler

from .base import BaseTimerAction

from ..entities import CountDownTimer

from ..utils import Interval


addonHandler.initTranslation()


class CountDownTimerAction(BaseTimerAction):

    def __init__(self):
        super().__init__()

        self.timer: CountDownTimer | None = None

    @property
    def name(self) -> str:
        return _("Countdown timer")

    @property
    def is_started(self) -> bool:
        return self.timer and self.timer.is_running

    @property
    def is_settings(self) -> bool:
        return self.timer and not self.timer.is_running

    def create(self):
        self.timer = CountDownTimer()

    def additional(self) -> str:
        if not self.timer:
            self.create()

        return self.timer.next_time_unit()

    def press_1(self) -> str:
        if not self.timer:
            self.create()

        return self.timer.get()

    def press_2(self) -> str:
        if self.is_settings:
            time_period_str = self.timer.set_time_period()
            return "\n".join([_("Countdown timer time period set"), time_period_str])
        return super().press_2()
