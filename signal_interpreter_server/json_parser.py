# json_parser.py
import json
class JsonParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        # open the json file
        with open(file_path, "r") as json_file:
            # load the json file and save it to self.data
            self.data = json.load(json_file)
            return self.data

    def get_signal_title(self, identifier):
        # loop through all services in self.data
        # if the service ID is the identifier, return the title
        for p in self.data["services"]:
            if p["id"] == identifier:
                return p["title"]
