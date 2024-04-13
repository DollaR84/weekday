from itertools import cycle
import logging

import addonHandler

from .alarm import AlarmAction
from .countdown_timer import CountDownTimerAction
from .timer import TimerAction
from .signal import SignalAction
from .weekday import WeekdayAction

from ..utils import Saver


addonHandler.initTranslation()


class Solver:

    def __init__(self):
        self.actions: list = [
            WeekdayAction(),
            TimerAction(),
            CountDownTimerAction(),
            AlarmAction(),
            SignalAction(),
        ]

        self.saver: Saver = Saver()
        try:
            data = self.saver.load()
            for action in self.actions:
                action.load_data(data)
        except Exception as error:
            logging.error(error, exc_info=True)

        self.current_action = None
        self.action_generator = self._action_generator()

    def _action_generator(self) -> str:
        for action in cycle(self.actions):
            self.current_action = action
            yield self.current_action.name

    def change_mode(self) -> str:
        return next(self.action_generator)

    def save_data(self):
        data = {}
        for action in self.actions:
            data.update(action.save_data())
        self.saver.save(data)

    def additional(self) -> str:
        if not self.current_action:
            next(self.action_generator)

        text = self.current_action.additional()
        if not text:
            self.save_data()
            text = _("data saved")
        elif isinstance(self.current_action, SignalAction) or isinstance(self.current_action, WeekdayAction):
            self.save_data()
        return text

    def additional2(self, press_count: int) -> str:
        if not self.current_action:
            next(self.action_generator)

        self.current_action.additional2(press_count)

    def get(self, press_count: int) -> str:
        if not self.current_action:
            next(self.action_generator)

        text = self.current_action.get(press_count)

        if press_count == 3 or (
            press_count == 2 and isinstance(self.current_action, TimerAction)
        ):
            self.save_data()
        return text
