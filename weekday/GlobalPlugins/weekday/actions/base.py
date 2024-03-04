from abc import ABC, abstractmethod


class BaseAction(ABC):

    def __init__(self):
        pass

    @property
    def is_started(self) -> bool:
        raise NotImplementedError

    @property
    def is_settings(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def additional(self) -> str:
        raise NotImplementedError

    def get(self, press_count: int) -> str:
        if hasattr(self, f"press_{press_count}"):
            return getattr(self, f"press_{press_count}")()
        return ""


class BaseTimerAction(BaseAction, ABC):

    def start(self) -> str:
        if not self.timer:
            self.create()
        return self.timer.start()

    def stop(self) -> str:
        text = self.timer.stop()
        self.timer = None
        return text

    def press_2(self) -> str:
        if self.is_started:
            text = self.timer.interrupt()
            self.need_save_data = True
        else:
            text = self.start()
        return text

    def press_3(self) -> str:
        if self.is_started:
            text = self.stop()
        else:
            text = self.start()
        return text
