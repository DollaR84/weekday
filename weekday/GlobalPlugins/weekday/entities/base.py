from abc import ABC, abstractmethod
from datetime import timedelta


class BaseTimer(ABC):

    def __init__(self):
        self.resume_period: timedelta | None = None

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
