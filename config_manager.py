import configparser
from configparser import RawConfigParser
class ConfigManager:
    '''
    Pending: create configuration files for this project
    '''

    def __init__(self, config_path) -> RawConfigParser:

        self.configParser = configparser.RawConfigParser()   
        configFilePath = config_path
        self.configParser.read(configFilePath)

    def get_config(self):
        return self.configParser
