import os
import pickle

import globalVars


class Saver:

    def __init__(self):
        base_dir = globalVars.appArgs.configPath
        self.file_name = os.path.join(base_dir, "weekday.dat")

    def save(self, data: dict):
        with open(self.file_name, "wb") as data_file:
            pickle.dump(data, data_file)

    def load(self) -> dict:
        data = {}
        with open(self.file_name, "rb") as data_file:
            data = pickle.load(data_file)

        return data
