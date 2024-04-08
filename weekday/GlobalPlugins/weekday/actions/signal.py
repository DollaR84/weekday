import addonHandler

from .base import BaseAction

from ..entities import Signal


addonHandler.initTranslation()


class SignalAction(BaseAction):

    def create(self):
        self.entity: Signal = Signal()

    @property
    def name(self) -> str:
        return _("Signal")

    @property
    def is_started(self) -> bool:
        return True

    @property
    def is_settings(self) -> bool:
        return False

    def press_1(self) -> str:
        if not self.entity:
            self.create()

        return self.entity.get()

    def additional(self) -> str:
        return self.entity.change_type()
