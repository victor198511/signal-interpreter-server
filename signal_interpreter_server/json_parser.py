# json_parser.py
# pylint: disable=missing-class-docstring

import os
import logging.config
import logging
import json
import yaml
from flask import abort
from signal_interpreter_server.exceptions import JsonParserError


CURR_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_SETTINGS_PATH = os.path.join(CURR_DIR, "..", "cfg", "log_settings.yaml")

with open(LOG_SETTINGS_PATH, "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

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
            # logger.exception("Exception occurred %s ", err)
            logger.warning("Exception occurred %s ", err)
            logger.info("Raising exception: %s", JsonParserError)
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
                logger.info("Raising exception: %s", JsonParserError)
                raise JsonParserError
        except JsonParserError as err:
            # print(f"Got exception: Signal with ID: {identifier} was not found in database")
            logger.exception("Exception occurred: %s ", err)
            logger.error("Requested signal not found in database, signal ID: %s ", identifier)
            logger.info("Aborting server ...")
            abort(404, description="Signal not found")
        return service_title

#            else:
#                service_title = str("No signal title found for this id")
