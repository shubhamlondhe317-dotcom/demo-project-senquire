import configparser
import os

def read_config(section, key):
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "../config.ini"))
    return config.get(section, key)
