# routes.py

import logging

from flask import Flask, request, jsonify, abort
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.exceptions import JsonParserError

logger = logging.getLogger(__name__)

signal_interpreter_app = Flask(__name__)
json_parser = JsonParser()


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    data = request.get_json()
    # print(data['signal'])
    id_of_requested_signal = data['signal']
    signal_title = json_parser.get_signal_title(id_of_requested_signal)
    try:
        if signal_title == 'None':
            logger.info("Raising exception: %s", JsonParserError)
            raise JsonParserError
    except JsonParserError as err:
        logger.exception("Exception occurred: %s ", err)
        logger.error("Signal not found in database, signal ID: %s ", id_of_requested_signal)
        logger.info("Aborting server ...")
        abort(404, description="Signal not found")

    return jsonify(signal_title)
