import configparser
import os

class ConfigReader:
    @staticmethod
    def read_config(section, key):
        config = configparser.ConfigParser()
        config_path = r"/Users/piyushshdravyakar/PycharmProjects/PythonProject/e2e-tests/config/config.ini"
        config.read(config_path)
        return config[section][key]


