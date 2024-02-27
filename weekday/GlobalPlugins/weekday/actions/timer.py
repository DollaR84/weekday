from .base import BaseAction

from ..entities import Timer


class TimerAction(BaseAction):

    def __init__(self):
        self.timer: Timer | None = None

    @property
    def is_started(self) -> bool:
        return bool(self.timer)

    def start(self) -> str:
        self.timer = Timer()
        return self.timer.start()

    def press_1(self) -> str:
        return self.timer.get()

    def press_2(self) -> str:
        if self.timer:
            text = self.timer.stop()
            self.timer = None
        else:
            text = self.start()
        return text
