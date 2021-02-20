# conftest.py

import pytest

from signal_interpreter_server.parser_factory import ParserFactory


@pytest.fixture
def parser_factory_instance():
    my_parser_factory = ParserFactory()
    return my_parser_factory
