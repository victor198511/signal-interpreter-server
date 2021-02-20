# main.py

from argparse import ArgumentParser
from signal_interpreter_server.routes import signal_interpreter_app
from signal_interpreter_server.routes import parser_factory
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.xml_parser import XmlParser


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()


def main():
    args = parse_arguments()

    if "xml" in args.file_path:
        parser_factory.set_signal_database_format("XML")
        parser_factory.register_format("XML", XmlParser)
    if "json" in args.file_path:
        parser_factory.set_signal_database_format("JSON")
        parser_factory.register_format("JSON", JsonParser)

    parser = parser_factory.get_parser()
    parser.load_file(args.file_path)
    signal_interpreter_app.run()


def init():
    if __name__ == "__main__":
        main()


init()
