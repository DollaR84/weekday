import addonHandler

from .base import BaseTimerAction

from ..entities import Timer


addonHandler.initTranslation()


class TimerAction(BaseTimerAction):

    @property
    def name(self) -> str:
        return _("Timer")

    @property
    def is_started(self) -> bool:
        return bool(self.entity)

    @property
    def is_settings(self) -> bool:
        return False

    def create(self):
        self.entity = Timer()

    def press_1(self) -> str:
        if self.is_started:
            return self.entity.get()

        else:
            return self.start()
