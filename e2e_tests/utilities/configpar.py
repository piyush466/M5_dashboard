import configparser
import os

class ConfigReader:
    @staticmethod
    def read_config(section, key):
        config = configparser.ConfigParser()
        config_path = r"//config/config.ini"
        config.read(config_path)
        return config[section][key]


