from abc import ABC, abstractmethod


class BaseAction(ABC):

    def __init__(self):
        self.entity = None

    @property
    def is_started(self) -> bool:
        raise NotImplementedError

    @property
    def is_settings(self) -> bool:
        raise NotImplementedError

    def additional(self) -> str:
        return None

    def additional2(self, press_count: int):
        return

    def get(self, press_count: int) -> str:
        if hasattr(self, f"press_{press_count}"):
            return getattr(self, f"press_{press_count}")()
        return ""

    def save_data(self) -> dict:
        data = self.entity.save_data() if self.entity else {}
        return {self.__class__.__name__: data}

    def load_data(self, data: dict):
        data_ = data.get(self.__class__.__name__)
        if not self.entity:
            self.create()
        self.entity.load_data(data_)


class BaseTimerAction(BaseAction, ABC):

    def start(self) -> str:
        if not self.entity:
            self.create()
        return self.entity.start()

    def stop(self) -> str:
        text = self.entity.stop()
        self.entity = None
        return text

    def press_2(self) -> str:
        if self.is_started:
            text = self.entity.interrupt()
        else:
            text = self.start()
        return text

    def press_3(self) -> str:
        if self.is_started:
            text = self.stop()
        else:
            text = self.start()
        return text


class BaseAlarmAction(BaseAction, ABC):

    @property
    def is_started(self) -> bool:
        return self.entity and self.entity.is_running

    @property
    def is_settings(self) -> bool:
        return self.entity and not self.entity.is_running

    def additional(self) -> str:
        if not self.entity:
            self.create()

        return self.entity.next_time_unit()

    def press_1(self) -> str:
        if not self.entity:
            self.create()

        return self.entity.get()

    def press_2(self) -> str:
        return self.press_1()
