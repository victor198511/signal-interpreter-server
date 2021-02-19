import pytest
from unittest.mock import patch, mock_open
from signal_interpreter_server.parser_factory import ParserFactory
from signal_interpreter_server.xml_parser import XmlParser


class MockParser:
    def parser(self):
        pass


parser_factory_instance = ParserFactory()


def test_register_format(parser_factory_instance):
    parser_factory_instance.register_format("XML", MockParser)
    assert isinstance(parser_factory_instance._parsers["XML"], MockParser)
