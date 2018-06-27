# -*- coding: utf-8 -*-
import configparser
import ast

class RobotConfig:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.sensors = []
        self._load()

    def _load(self):
        for section in self.config.sections():
            if ('TYPE' in self.config[section] and self.config[section]['TYPE'] == 'SENSOR'):
                self.sensors.append(section)

    def get_section(self, section):
        return self.config[section]