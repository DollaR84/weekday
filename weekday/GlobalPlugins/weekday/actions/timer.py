import addonHandler

from .base import BaseTimerAction

from ..entities import Timer


addonHandler.initTranslation()


class TimerAction(BaseTimerAction):

    def __init__(self):
        super().__init__()

        self.timer: Timer | None = None

    @property
    def name(self) -> str:
        return _("Timer")

    @property
    def is_started(self) -> bool:
        return bool(self.timer)

    @property
    def is_settings(self) -> bool:
        return False

    def create(self):
        self.timer = Timer()

    def additional(self) -> str:
        return self.press_1()

    def press_1(self) -> str:
        if self.is_started:
            return self.timer.get()

        else:
            return self.start()
