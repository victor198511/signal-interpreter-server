# pylint: disable=missing-class-docstring

from unittest.mock import patch
import pytest
from signal_interpreter_server.parser_factory import ParserFactory


class MockParser:
    def parser(self):
        pass


@patch.object(ParserFactory, "get_signal_database_format", return_value="FORMAT")
@patch.object(ParserFactory, "register_format")
@patch.object(ParserFactory, "get_parser", return_value=MockParser)
def test_set_signal_database_format(mock_get_parser, mock_register_format,
                                    mock_get_signal_database_format, parser_factory_instance):
    parser_factory_instance.set_signal_database_format("FORMAT")
    assert parser_factory_instance._signal_database_format == "FORMAT"


@patch.object(ParserFactory, "set_signal_database_format")
@patch.object(ParserFactory, "register_format")
@patch.object(ParserFactory, "get_parser", return_value=MockParser)
def test_get_signal_database_format(mock_get_parser, mock_register_format,
                                    mock_set_signal_database_format, parser_factory_instance):
    parser_factory_instance._signal_database_format = "FORMAT"
    assert parser_factory_instance.get_signal_database_format() == "FORMAT"


@patch.object(ParserFactory, "set_signal_database_format")
@patch.object(ParserFactory, "get_signal_database_format", return_value="FORMAT")
@patch.object(ParserFactory, "get_parser", return_value=MockParser)
def test_register_format(mock_get_parser, mock_set_signal_database_format,
                         mock_get_signal_database_format, parser_factory_instance):
    parser_factory_instance.register_format("FORMAT", MockParser)
    assert isinstance(parser_factory_instance._parsers["FORMAT"], MockParser)


@patch.object(ParserFactory, "set_signal_database_format")
@patch.object(ParserFactory, "get_signal_database_format", return_value="FORMAT")
@patch.object(ParserFactory, "register_format")
def test_get_parser(mock_register_format, mock_get_signal_database_format,
                    mock_set_signal_database_format, parser_factory_instance):
    parser_factory_instance._signal_database_format = "FORMAT"
    parser_factory_instance._parsers = {"FORMAT": MockParser}
    assert parser_factory_instance.get_parser() == parser_factory_instance._parsers["FORMAT"]
    parser_factory_instance._signal_database_format = "UNKNOWN"
    with pytest.raises(ValueError):
        parser_factory_instance.get_parser()
