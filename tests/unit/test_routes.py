# pylint: disable=missing-class-docstring

from unittest.mock import patch

from signal_interpreter_server.routes import ParserFactory
from signal_interpreter_server.routes import signal_interpreter_app


class MockParser:
    @classmethod
    def get_signal_title(cls):
        return "None"


@patch('signal_interpreter_server.routes.abort')
@patch.object(ParserFactory, "get_signal_database_format")
@patch.object(MockParser, "get_signal_title")
@patch.object(ParserFactory, "get_parser", return_value=MockParser)
def test_interpret_signal(mock_get_parser, mock_get_signal_title, mock_get_signal_database_format, mock_abort):
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        my_payload = {"signal": "27"}
        mock_get_signal_database_format.return_value = "FORMAT"
        mock_get_signal_title.return_value = "Security Access"
        response = client.post("/", json=my_payload)
        assert response.get_json() == "Security Access"
        mock_get_signal_database_format.return_value = "JSON"
        mock_get_signal_title.return_value = "None"
        client.post("/", json=my_payload)
        mock_abort.assert_called_once_with(404, description="Signal not found")


@patch('signal_interpreter_server.routes.abort')
@patch.object(ParserFactory, "get_signal_database_format")
@patch.object(MockParser, "get_signal_title")
@patch.object(ParserFactory, "get_parser", return_value=MockParser)
def test_interpret_signal_xml(mock_get_parser, mock_get_signal_title, mock_get_signal_database_format, mock_abort):
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        my_payload = {"signal": "27"}
        mock_get_signal_database_format.return_value = "XML"
        mock_get_signal_title.return_value = "None"
        client.post("/", json=my_payload)
        mock_abort.assert_called_once_with(404, description="Signal not found")
