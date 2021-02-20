import json
from unittest.mock import patch, mock_open
import pytest
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.exceptions import JsonParserError

json_parser = JsonParser()
json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}


def test_load_file():
    with patch("builtins.open", mock_open(read_data=json.dumps({"services": [{"title": "ECU Reset", "id": "11"}]}))):
        assert json_parser.load_file("my_file_path") == {"services": [{"title": "ECU Reset", "id": "11"}]}
    with pytest.raises(JsonParserError):
        json_parser.load_file("my_file_path")


json_parser2 = JsonParser()
json_parser2.data = {"services": [{"title": "ECU Reset", "id": "11"}, {"title": "Security Access", "id": "27"},
                                  {"title": "Tester Present", "id": "3E"}, {"title": "None", "id": "20"}]}


@pytest.mark.parametrize("item, expected_title", [
    ("11", "ECU Reset"),
    ("27", "Security Access"),
    ("3E", "Tester Present"),
    ("20", "None"),
])
def test_get_signal_title(item, expected_title):
    assert json_parser2.get_signal_title(item) == expected_title
