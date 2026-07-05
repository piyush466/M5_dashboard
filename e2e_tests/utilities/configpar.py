# import configparser
# import os
#
# class ConfigReader:
#     @staticmethod
#     def read_config(section, key):
#         config = configparser.ConfigParser()
#         config_path = r"//config/config.ini"
#         config.read(config_path)
#         return config[section][key]
#
#
import configparser
import os

class ConfigReader:

    @staticmethod
    def read_config(section, key):
        config = configparser.ConfigParser()

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, "config", "config.ini")

        config.read(config_path)

        return config[section][key]

