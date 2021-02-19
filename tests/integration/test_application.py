import os
import sys
from unittest.mock import patch

from signal_interpreter_server.main import main, signal_interpreter_app

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
FIXTURE_PATH = os.path.join(CURR_DIR, "fixture", "test_basic.json")


@patch.object(sys, "argv", ["signal_interpreter_server", "--file_path", FIXTURE_PATH])
@patch.object(signal_interpreter_app, "run")
def test_application(mock_run):
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()
    main()
    mock_run.assert_called_once()

    with my_app_instance as client:
        my_payload = {"signal": "27"}
        response = client.post("/", json=my_payload)
        assert response.get_json() == "Security Access"


FIXTURE_PATH = os.path.join(CURR_DIR, "fixture", "test_basic.xml")


@patch.object(sys, "argv", ["signal_interpreter_server", "--file_path", FIXTURE_PATH])
@patch.object(signal_interpreter_app, "run")
def test_application(mock_run):
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()
    main()
    mock_run.assert_called_once()

    with my_app_instance as client:
        my_payload = {"signal": "27"}
        response = client.post("/", json=my_payload)
        assert response.get_json() == "Security Access"
