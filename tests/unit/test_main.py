from unittest.mock import patch, mock_open
from signal_interpreter_server.main import main, parse_arguments, ArgumentParser
from signal_interpreter_server.json_parser import JsonParser
import json


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


def test_load_file():
    with patch("builtins.open", mock_open(read_data=json.dumps({"services": [{"title": "ECU Reset", "id": "11"}]}))):
        assert json_parser.load_file("my_file_path") == {"services": [{"title": "ECU Reset", "id": "11"}]}


def test_get_signal_title():
    assert json_parser.get_signal_title("11") == "ECU Reset"


@patch("signal_interpreter_server.main.signal_interpreter_app.run")
@patch.object(JsonParser, "load_file")
@patch("signal_interpreter_server.main.parse_arguments")
def test_main(mock_parse_arguments, mock_load_file, mock_run):
    mock_parse_arguments.return_value = MockArgs
    mock_load_file.return_value = {"services": [{"title": "ECU Reset", "id": "11"}]}
    main()
    # mock_load_file.assert_called_with(MockArgs.file_path)
    mock_run.assert_called_once()
