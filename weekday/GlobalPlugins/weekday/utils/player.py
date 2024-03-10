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

        base_dir = os.path.split(os.path.dirname(__file__))[:-1][0]
        file_name = os.path.join(base_dir, cls._folder_path, cls._names[sound_num])
        winsound.PlaySound(file_name, winsound.SND_ASYNC)
