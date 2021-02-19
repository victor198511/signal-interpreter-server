from unittest.mock import patch
from signal_interpreter_server.main import main, init, parse_arguments, ArgumentParser
from signal_interpreter_server.json_parser import JsonParser


class MockArgs:
    file_path = "path/to/file"


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    assert parse_arguments() == MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file_path")


@patch("signal_interpreter_server.main.signal_interpreter_app.run")
@patch.object(JsonParser, "load_file")
@patch("signal_interpreter_server.main.parse_arguments")
def test_main(mock_parse_arguments, mock_load_file, mock_run):
    mock_parse_arguments.return_value = MockArgs
    mock_load_file.return_value = {"services": [{"title": "ECU Reset", "id": "11"}]}
    main()
    # mock_load_file.assert_called_with(MockArgs.file_path)
    mock_run.assert_called_once()


@patch("signal_interpreter_server.main.main")
@patch("signal_interpreter_server.main.__name__", "__main__")
def test_init(mock_main):
    init()
    mock_main.assert_called_once()
