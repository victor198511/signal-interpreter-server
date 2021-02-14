from unittest.mock import patch

from signal_interpreter_server.routes import JsonParser
from signal_interpreter_server.routes import signal_interpreter_app


@patch('signal_interpreter_server.routes.abort')
@patch.object(JsonParser, "get_signal_title")
def test_interpret_signal(mock_get_signal_title, mock_abort):
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        my_payload = {"signal": "27"}
        mock_get_signal_title.return_value = "Security Access"
        response = client.post("/", json=my_payload)
        assert response.get_json() == "Security Access"
        mock_get_signal_title.return_value = "None"
        client.post("/", json=my_payload)
        mock_abort.assert_called_once_with(404, description="Signal not found")
