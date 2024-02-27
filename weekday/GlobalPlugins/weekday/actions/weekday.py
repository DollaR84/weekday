from .base import BaseAction

from ..entities import Weekday


class WeekdayAction(BaseAction):

    def __init__(self):
        self.weekday: Weekday = Weekday

    def is_started(self) -> bool:
        return True

    def press_1(self) -> str:
        return self.weekday.get_week_day()
