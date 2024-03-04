from itertools import cycle

import addonHandler

from .countdown_timer import CountDownTimerAction
from .timer import TimerAction
from .signal import SignalAction
from .weekday import WeekdayAction


addonHandler.initTranslation()


class Solver:

    def __init__(self):
        self.actions: list = [
            WeekdayAction(),
            TimerAction(),
            CountDownTimerAction(),
            SignalAction(),
        ]

        self.current_action = None
        self.action_generator = self._action_generator()

    def _action_generator(self) -> str:
        for action in cycle(self.actions):
            self.current_action = action
            yield self.current_action.name

    def change_mode(self) -> str:
        return next(self.action_generator)

    def additional(self) -> str:
        if not self.current_action:
            next(self.action_generator)

        return self.current_action.additional()

    def get(self, press_count: int) -> str:
        if not self.current_action:
            next(self.action_generator)

        return self.current_action.get(press_count)
