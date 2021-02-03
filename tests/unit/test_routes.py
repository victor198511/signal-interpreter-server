from unittest.mock import patch
from signal_interpreter_server.routes import signal_interpreter_app
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.routes import JsonParser


@patch.object(JsonParser, "get_signal_title")
def test_my_routes_function(mock_get_signal_title):
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        my_payload = {"signal": "27"}
        mock_get_signal_title.return_value = "Security Access"
        response = client.post("/", json=my_payload)
        assert response.get_json() == "Security Access"
