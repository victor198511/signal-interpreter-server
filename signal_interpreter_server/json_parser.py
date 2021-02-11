# json_parser.py
# pylint: disable=missing-class-docstring

import json
from flask import abort
from signal_interpreter_server.exceptions import JsonParserError


class JsonParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        # open the json file
        try:
            with open(file_path, "r") as json_file:
                # load the json file and save it to self.data
                self.data = json.load(json_file)
                return self.data
        except FileNotFoundError as err:
            raise JsonParserError("Json database file is not found") from err

    def get_signal_title(self, identifier):
        # loop through all services in self.data
        # if the service ID is the identifier, return the title
        # service_title = "No signal title found for this id"
        service_title = "Null"
        for service in self.data["services"]:
            if service["id"] == identifier:
                service_title = service["title"]

        try:
            if service_title == "Null":
                raise JsonParserError
        except JsonParserError:
            abort(404, description="Signal not found")
        return service_title

#            else:
#                service_title = str("No signal title found for this id")
