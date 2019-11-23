import json

class ConfigFile:
    def __init__(self, filename):
        with open(filename) as json_file:
            self.conf = json.load(json_file)

    def get_value(self, key):
        return self.conf[key]
