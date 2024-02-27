from abc import ABC


class BaseAction(ABC):

    @property
    def is_started(self) -> bool:
        raise NotImplementedError

    def get(self, press_count: int) -> str:
        if hasattr(self, f"press_{press_count}"):
            return getattr(self, f"press_{press_count}")()
        return ""
