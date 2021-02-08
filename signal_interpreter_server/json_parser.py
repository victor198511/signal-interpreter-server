# json_parser.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

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
        service_title = "No signal title found for this id"
        for service in self.data["services"]:
            if service["id"] == identifier:
                service_title = service["title"]
#            else:
#                service_title = str("No signal title found for this id")
        return service_title
