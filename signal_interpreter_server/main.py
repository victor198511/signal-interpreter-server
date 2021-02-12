# main.py

import logging.config
import os

from argparse import ArgumentParser
import yaml
from signal_interpreter_server.routes import signal_interpreter_app
from signal_interpreter_server.routes import json_parser

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_SETTINGS_PATH = os.path.join(CURR_DIR, "..", "cfg", "log_settings.yaml")

with open(LOG_SETTINGS_PATH, "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)


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


def init():
    if __name__ == "__main__":
        main()


init()

# if __name__ == "__main__":
#     main()
