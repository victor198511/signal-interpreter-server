# json_parser.py
# pylint: disable=missing-class-docstring

import logging
import json
from signal_interpreter_server.exceptions import JsonParserError

logger = logging.getLogger(__name__)


class JsonParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        # open the json file
        logger.info("Opening json database file: %s", file_path)
        try:
            with open(file_path, "r") as json_file:
                # load the json file and save it to self.data
                logger.info("Loading json database file: %s", file_path)
                self.data = json.load(json_file)
                return self.data
        except FileNotFoundError as err:
            logger.warning("Exception occurred %s ", err)
            logger.info("Raising exception: %s", JsonParserError)
            raise JsonParserError("Json database file is not found") from err

    def get_signal_title(self, identifier):
        # loop through all services in self.data
        service_title = "None"
        for service in self.data["services"]:
            if service["id"] == identifier:
                service_title = service["title"]
        return service_title
