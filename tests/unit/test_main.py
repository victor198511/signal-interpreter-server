from unittest.mock import patch, mock_open
from signal_interpreter_server.main import parse_arguments, ArgumentParser
from signal_interpreter_server.json_parser import JsonParser


class MockArgs:
    file_path = "path/to/file"


json_parser = JsonParser()
json_parser.data = {"services": [{"title": "ECU Reset", "id": "11"}]}


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    assert parse_arguments() == MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file_path")


#def test_load_file():
#    with patch("builtins.open", mock_open(read_data={"services": [{"title": "ECU Reset", "id": "11"}]})):
#        assert json_parser.load_file("signal_database.json") == {"services": [{"title": "ECU Reset", "id": "11"}]}
