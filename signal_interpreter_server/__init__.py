
import os
import logging.config
import yaml

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_SETTINGS_PATH = os.path.join(CURR_DIR, "..", "cfg", "log_settings.yaml")

with open(LOG_SETTINGS_PATH, "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
