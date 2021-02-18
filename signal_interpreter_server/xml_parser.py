# xml_parser.py
# pylint: disable=missing-class-docstring

import logging
import xml.etree.ElementTree as ET
import xmltodict
from signal_interpreter_server.exceptions import XmlParserError

logger = logging.getLogger(__name__)


class XmlParser:
    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        # open and load data from xml file
        logger.info("Opening xml database file: %s", file_path)
        try:
            tree = ET.parse(file_path)
            data = tree.getroot()
            xml_string = ET.tostring(data, encoding="utf-8", method="xml")
            self.data = dict(xmltodict.parse(xml_string))
            return self.data
        except FileNotFoundError as err:
            logger.warning("Exception occurred %s ", err)
            logger.info("Raising exception: %s", XmlParserError)
            raise XmlParserError("Xml database file is not found") from err

    def get_signal_title(self, identifier):
        # loop through all services in self.data
        service_title = "None"
        for services in self.data["services"].values():
            for service in services:
                if service["@id"] == identifier:
                    service_title = service["title"]
        return service_title
