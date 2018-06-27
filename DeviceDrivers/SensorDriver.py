# -*- coding: utf-8 -*-
import ast

from I2C.I2C import I2CBus

class SensorDriver:

    def __init__(self, config):
        self.config = config
        self.sensors = ast.literal_eval(config['SENSORS'])

    def sensors(self):
        return self.sensors

    def actualize_sensors(self):
        keys = self.sensors.keys()
        for key in keys:
            self.actualize_sensor(self.sensors[key])

    def actualize_sensor(self, device):
        i2c = I2CBus(device['TYPE'])
        for sensor in device['SENSORS']
            i2c.readList(sendor['cmdI2c'])
