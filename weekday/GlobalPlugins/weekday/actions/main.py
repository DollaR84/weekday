from .timer import TimerAction

from .weekday import WeekdayAction


class SolverAction:

    def __init__(self):
        self.timer: TimerAction = TimerAction()
        self.weekday: WeekdayAction = WeekdayAction()

    def get(self, press_count: int) -> str:
        if press_count == 2 or self.timer.is_started:
            return self.timer.get(press_count)

        return self.weekday.get(press_count)
