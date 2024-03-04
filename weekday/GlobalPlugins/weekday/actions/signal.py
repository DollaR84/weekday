import addonHandler

from .base import BaseAction

from ..entities import Signal


addonHandler.initTranslation()


class SignalAction(BaseAction):

    def __init__(self):
        super().__init__()

        self.signal: Signal = Signal()

    @property
    def name(self) -> str:
        return _("Signal")

    @property
    def is_started(self) -> bool:
        return True

    @property
    def is_settings(self) -> bool:
        return False

    def additional(self) -> str:
        return self.press_1()

    def press_1(self) -> str:
        return self.signal.get()
