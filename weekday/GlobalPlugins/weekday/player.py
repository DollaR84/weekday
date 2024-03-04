import os
import winsound


class Player:
    _folder_path = "sounds"

    _names = {
        0: "Signal.wav",
        1: "Crystals.wav",
        2: "Hillside.wav",
    }

    @classmethod
    def play(cls, sound_num: int):
        if not cls._names.get(sound_num):
            return

        file_name = os.path.join(os.path.dirname(__file__), cls._folder_path, cls._names[sound_num])
        winsound.PlaySound(file_name, winsound.SND_ASYNC)
