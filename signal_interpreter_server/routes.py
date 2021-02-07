# routes.py
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

from flask import Flask, request, jsonify
from signal_interpreter_server.json_parser import JsonParser

signal_interpreter_app = Flask(__name__)
json_parser = JsonParser()


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    data = request.get_json()
    # print(data['signal'])
    id_of_requested_signal = data['signal']
    signal_title = json_parser.get_signal_title(id_of_requested_signal)
    return jsonify(signal_title)
