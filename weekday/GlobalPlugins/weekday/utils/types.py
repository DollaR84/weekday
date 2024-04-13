from enum import Enum


class TimeUnit(Enum):
    DAYS = "days"
    HOURS = "hours"
    MINUTES = "minutes"
    SECONDS = "seconds"


class SignalType(Enum):
    SOUND = "sound"
    SPEECH = "speech"
    SOUND_AND_SPEECH = "sound_and_speech"
    DISABLED = "disabled"


class DateEventType(Enum):
    SOURCE1 = "source1"
    SOURCE2 = "source2"
    SOURCE12 = "source12"
    DISABLED = "disabled"
