from datetime import timedelta
from typing import Union


import addonHandler


addonHandler.initTranslation()


class Interval:

    localisations: dict = {
        "one_days_ends": _("one_day"),
        "one_hours_ends": _("one_hour"),
        "one_minutes_ends": _("one_minute"),
        "one_seconds_ends": _("one_second"),
        "2_to_4_days_ends": _("2_to_4_days"),
        "5_more_days_ends": _("5_more_days"),
        "2_to_4_hours_ends": _("2_to_4_hours"),
        "5_more_hours_ends": _("5_more_hours"),
        "2_to_4_minutes_ends": _("2_to_4_minutes"),
        "5_more_minutes_ends": _("5_more_minutes"),
        "2_to_4_seconds_ends": _("2_to_4_seconds"),
        "5_more_seconds_ends": _("5_more_seconds"),
    }

    @classmethod
    def get_text(cls, key: str, time_unit: str, value: int):
        unit = cls.localisations.get(f"{key}_{time_unit}_ends", "")
        return f"{value} {unit}"

    @classmethod
    def to_str(cls, interval: Union[timedelta, float]) -> str:
        if isinstance(interval, float):
            interval = timedelta(seconds=interval)
        time_interval_data = {
            "days": round(interval.days),
            "hours": round(interval.total_seconds() % 86400 // 3600),
            "minutes": round(interval.total_seconds() % 86400 % 3600 // 60),
            "seconds": round(interval.total_seconds() % 86400 % 3600 % 60)
        }
        texts = list()
        time_units = time_interval_data.keys()

        for time_unit in time_units:
            value = time_interval_data[time_unit]
            if value <= 0:
                continue
            elif value in range(5, 21) or value % 10 in list(range(5, 10)) + [0]:
                text = cls.get_text("5_more", time_unit, value)
            elif value % 10 == 1:
                text = cls.get_text("one", time_unit, value)
            elif value % 10 in range(2, 5):
                text = cls.get_text("2_to_4", time_unit, value)
            else:
                text = ""
            texts.append(text)
        time_interval = " ".join(texts)
        return time_interval
