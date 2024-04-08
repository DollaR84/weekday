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
    OFF = "off"
