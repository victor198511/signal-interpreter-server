from unittest.mock import patch, mock_open
from signal_interpreter_server.json_parser import JsonParser
import json

json_parser = JsonParser()
json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}


def test_load_file():
    with patch("builtins.open", mock_open(read_data=json.dumps({"services": [{"title": "ECU Reset", "id": "11"}]}))):
        assert json_parser.load_file("my_file_path") == {"services": [{"title": "ECU Reset", "id": "11"}]}


def test_get_signal_title():
    assert json_parser.get_signal_title("11") == "ECU Reset"
