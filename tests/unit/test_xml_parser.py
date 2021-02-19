from unittest.mock import patch, mock_open

import pytest

from signal_interpreter_server.exceptions import XmlParserError
from signal_interpreter_server.xml_parser import XmlParser

xml_parser = XmlParser()
xml_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}


def test_load_file():
    with patch("builtins.open", mock_open(read_data=xml.dumps({"services": [{"title": "ECU Reset", "id": "11"}]}))):
        assert xml_parser.load_file("my_file_path") == {"services": [{"title": "ECU Reset", "id": "11"}]}
    with pytest.raises(XmlParserError):
        xml_parser.load_file("my_file_path")


xml_parser2 = XmlParser()
xml_parser2.data = {"services": [{"title": "ECU Reset", "id": "11"}, {"title": "Security Access", "id": "27"},
                                  {"title": "Tester Present", "id": "3E"}, {"title": "None", "id": "20"}]}


@pytest.mark.parametrize("item, expected_title", [
    ("11", "ECU Reset"),
    ("27", "Security Access"),
    ("3E", "Tester Present"),
    ("20", "None"),
])
def test_get_signal_title(item, expected_title):
    assert xml_parser2.get_signal_title(item) == expected_title
