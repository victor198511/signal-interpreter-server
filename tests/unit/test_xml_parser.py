from unittest.mock import patch

import pytest

from signal_interpreter_server.exceptions import XmlParserError
from signal_interpreter_server.xml_parser import XmlParser


@patch('xmltodict.parse')
@patch("xml.etree.ElementTree.tostring")
@patch("xml.etree.ElementTree.parse")
def test_load_file_valid_file(mock_parse, mock_to_string, mock_xml_to_dict_parse):
    xml_parser = XmlParser()
    xml_parser.data = {"services": {"service": [{"title": "ECU Reset", "@id": "11"}]}}

    xml_parser.load_file("my_file_path")
    mock_parse.assert_called_with("my_file_path")
    mock_to_string.assert_called_once()
    mock_xml_to_dict_parse.assert_called_once()


def test_load_file_invalid_file():
    xml_parser1 = XmlParser()
    xml_parser1.data = {"services": {"service": [{"title": "ECU Reset", "@id": "11"}]}}

    with pytest.raises(XmlParserError):
        xml_parser1.load_file("my_file_path1")


xml_parser2 = XmlParser()
xml_parser2.data = {"services": {"service": [{"title": "ECU Reset", "@id": "11"},
                                             {"title": "Security Access", "@id": "27"},
                                             {"title": "Tester Present", "@id": "3E"}, {"title": "None", "@id": "19"}]}}


@pytest.mark.parametrize("item, expected_title", [
    ("11", "ECU Reset"),
    ("27", "Security Access"),
    ("3E", "Tester Present"),
    ("19", "None"),
])
def test_get_signal_title(item, expected_title):
    assert xml_parser2.get_signal_title(item) == expected_title
