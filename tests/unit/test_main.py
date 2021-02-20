# pylint: disable=missing-class-docstring

from unittest.mock import patch
from signal_interpreter_server.main import main, init, parse_arguments, ArgumentParser
from signal_interpreter_server.routes import ParserFactory


class MockArgs:
    file_path = "path/to/file"


class MockArgsXml:
    file_path = "path/to/file.xml"


class MockArgsJson:
    file_path = "path/to/file.json"


class MockParser:
    def load_file(self):
        pass


@patch.object(ArgumentParser, "add_argument")
@patch.object(ArgumentParser, "parse_args", return_value=MockArgs)
def test_parse_arguments(mock_parse_args, mock_add_argument):
    assert parse_arguments() == MockArgs
    mock_parse_args.assert_called_once()
    mock_add_argument.assert_called_with("--file_path")


@patch("signal_interpreter_server.main.signal_interpreter_app.run")
@patch.object(MockParser, "load_file")
@patch.object(ParserFactory, "get_parser", return_value=MockParser)
@patch.object(ParserFactory, "register_format")
@patch.object(ParserFactory, "set_signal_database_format")
@patch("signal_interpreter_server.main.parse_arguments")
def test_main_load_xml(mock_parse_arguments, mock_set_signal_database_format, mock_register_format,
                       mock_get_parser, mock_load_file, mock_run):
    mock_parse_arguments.return_value = MockArgsXml
    mock_load_file.return_value = {"services": [{"title": "ECU Reset", "id": "11"}]}
    main()
    mock_run.assert_called_once()


@patch("signal_interpreter_server.main.signal_interpreter_app.run")
@patch.object(MockParser, "load_file")
@patch.object(ParserFactory, "get_parser", return_value=MockParser)
@patch.object(ParserFactory, "register_format")
@patch.object(ParserFactory, "set_signal_database_format")
@patch("signal_interpreter_server.main.parse_arguments")
def test_main_load_json(mock_parse_arguments, mock_set_signal_database_format, mock_register_format,
                        mock_get_parser, mock_load_file, mock_run):
    mock_parse_arguments.return_value = MockArgsJson
    mock_load_file.return_value = {"services": [{"title": "ECU Reset", "id": "11"}]}
    main()
    mock_run.assert_called_once()


@patch("signal_interpreter_server.main.main")
@patch("signal_interpreter_server.main.__name__", "__main__")
def test_init(mock_main):
    init()
    mock_main.assert_called_once()
