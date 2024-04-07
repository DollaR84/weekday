from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from itertools import cycle
from typing import Union

from ..utils import Interval, types


class BaseEntity(ABC):

    def save_data(self) -> dict:
        return {}

    def load_data(self, data: dict):
        for key, value in data.items():
            setattr(self, key, value)


class BaseTimer(BaseEntity, ABC):

    def __init__(self):
        self.resume_period: timedelta | None = None
        super().__init__()

    def interrupt(self) -> str:
        if self.resume_period:
            text = self.resume()
        else:
            text = self.pause()
        return text

    @abstractmethod
    def pause(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def resume(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def start(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> str:
        raise NotImplementedError

    def save_data(self) -> dict:
        data = super().save_data()
        data.update(resume_period=self.resume_period)
        return data


class BaseAlarm(BaseEntity, ABC):

    def __init__(self):
        super().__init__()

        self.is_running: bool = False
        self.need_reminder: bool = False
        self.time_finished: datetime | None = None
        self.time_period: timedelta | int = 0
        self.time_unit: types.TimeUnit = types.TimeUnit.HOURS
        self.save_time: int = 0

        self.hours_current_value: int = 0
        self.minutes_current_value: int = 0
        self.seconds_current_value: int = 0

        self.time_unit_generator = self._time_unit_generator()
        self.time_hours_generator = self._time_hours_generator()
        self.time_minutes_generator = self._time_minutes_generator()
        self.time_seconds_generator = self._time_seconds_generator()

        next(self.time_unit_generator)
        next(self.time_hours_generator)
        next(self.time_minutes_generator)
        next(self.time_seconds_generator)

        self.track_process = None

    def _time_unit_generator(self) -> types.TimeUnit:
        for time_unit in cycle(types.TimeUnit):
            if time_unit == types.TimeUnit.DAYS:
                continue
            yield time_unit

    def _time_hours_generator(self) -> int:
        for hours in cycle(range(24)):
            yield hours

    def _time_minutes_generator(self) -> int:
        for minutes in cycle(range(0, 60, 5)):
            yield minutes

    def _time_seconds_generator(self) -> int:
        for seconds in cycle(range(0, 60, 5)):
            yield seconds

    def next_generator(self, time_unit: Union[types.TimeUnit, None] = None):
        if not time_unit:
            return next(self.time_unit_generator)
        elif time_unit == types.TimeUnit.HOURS:
            return next(self.time_hours_generator)
        elif time_unit == types.TimeUnit.MINUTES:
            return next(self.time_minutes_generator)
        elif time_unit == types.TimeUnit.SECONDS:
            return next(self.time_seconds_generator)

    def factor(self, time_unit: types.TimeUnit) -> int:
        if time_unit == types.TimeUnit.HOURS:
            return 60 * 60
        elif time_unit == types.TimeUnit.MINUTES:
            return 60
        elif time_unit == types.TimeUnit.SECONDS:
            return 1

    def calc_time_period(self, bounce: int):
        if self.time_unit == types.TimeUnit.HOURS:
            self.hours_current_value = (self.save_time - bounce) * self.factor(self.time_unit)
        elif self.time_unit == types.TimeUnit.MINUTES:
            self.minutes_current_value = (self.save_time - bounce) * self.factor(self.time_unit)
        elif self.time_unit == types.TimeUnit.SECONDS:
            self.seconds_current_value = (self.save_time - bounce) * self.factor(self.time_unit)

        self.time_period = timedelta(
            seconds=self.hours_current_value + self.minutes_current_value + self.seconds_current_value
        )

    def set_time_period(self) -> str:
        bounce = 1 if self.time_unit == types.TimeUnit.HOURS else 5
        self.calc_time_period(bounce)
        return Interval.to_str(self.time_period)

    def next_time_unit(self) -> str:
        self.time_unit = self.next_generator()
        time_period = self.next_generator(self.time_unit)
        time_period = time_period * self.factor(self.time_unit)
        return Interval.to_str(time_period, self.time_unit)

    def get(self):
        if self.is_running:
            now = datetime.now()
            return Interval.to_str(self.time_finished - now)

        self.save_time = self.next_generator(self.time_unit)
        return Interval.to_str(timedelta(seconds=self.save_time * self.factor(self.time_unit)), self.time_unit)

    def _stop(self):
        self.is_running = False
        self.track_process = None
        self.time_finished = None
        self.time_period = None

        self.save_time = 0
        self.hours_current_value = 0
        self.minutes_current_value = 0
        self.seconds_current_value = 0

    def save_data(self) -> dict:
        data = super().save_data()
        data.update(
            is_running=self.is_running,
            time_finished=self.time_finished,
            time_period=self.time_period,
            time_unit=self.time_unit,
            save_time=self.save_time,
            hours_current_value=self.hours_current_value,
            minutes_current_value=self.minutes_current_value,
            seconds_current_value=self.seconds_current_value,
        )
        return data
