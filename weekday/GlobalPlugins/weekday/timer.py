from datetime import datetime

from .interval import Interval


class Timer:

    def __init__(self):
        self.start = datetime.now()

    def get(self):
        now = datetime.now()
        return Interval.to_str(now - self.start)
