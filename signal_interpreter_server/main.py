# main.py
from signal_interpreter_server.routes import signal_interpreter_app
from signal_interpreter_server.routes import json_parser
from argparse import ArgumentParser


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--file_path")
    return parser.parse_args()


def main():
    args = parse_arguments()
    json_parser.load_file(args.file_path)
    # signal_database = json_parser.load_file(args.file_path)
    # signal_title = json_parser.get_signal_title("27")
    # print(signal_title)
    signal_interpreter_app.run()

if __name__ == "__main__":
    main()
