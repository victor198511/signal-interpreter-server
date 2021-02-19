# routes.py

import logging

from flask import Flask, request, jsonify, abort

from signal_interpreter_server.exceptions import JsonParserError, XmlParserError
from signal_interpreter_server.parser_factory import ParserFactory

logger = logging.getLogger(__name__)

signal_interpreter_app = Flask(__name__)
parser_factory = ParserFactory()


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    data = request.get_json()
    id_of_requested_signal = data['signal']
    parser = parser_factory.get_parser()
    signal_title = parser.get_signal_title(id_of_requested_signal)
    signal_database_format = parser_factory.get_signal_database_format()
    try:
        if (signal_title == "None") & (signal_database_format == "JSON"):
            logger.info("Raising exception: %s", JsonParserError)
            raise JsonParserError
        if (signal_title == "None") & (signal_database_format == "XML"):
            logger.info("Raising exception: %s", XmlParserError)
            raise XmlParserError
    except JsonParserError as err:
        logger.exception("Exception occurred: %s ", err)
        logger.error("Signal not found in database, signal ID: %s ", id_of_requested_signal)
        logger.info("Aborting server ...")
        abort(404, description="Signal not found")
    except XmlParserError as err:
        logger.exception("Exception occurred: %s ", err)
        logger.error("Signal not found in database, signal ID: %s ", id_of_requested_signal)
        logger.info("Aborting server ...")
        abort(404, description="Signal not found")
    return jsonify(signal_title)
