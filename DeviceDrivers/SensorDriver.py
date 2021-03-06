# -*- coding: utf-8 -*-
import ast
import time

from I2C.I2C import I2CBus

class SensorDriver:

    def __init__(self, config):
        self.config = config
        self.i2c = I2CBus(int(self.config['I2C_ADDRESS'], 0))
        self.sensors = ast.literal_eval(config['SENSORS'])

    def sensors(self):
        return self.sensors

    def actualize_sensors(self):
        keys = self.sensors.keys()
        for key in keys:
            time.sleep(0.1)
            self.actualize_sensor(self.sensors[key])

    def actualize_sensor(self, sensor):
        #Leemos y actualizamos en algun lugar
        self.get_sensor_data(sensor)
        #GUARDAR

    def get_sensor_data(self, sensor):
        return self.i2c.readBytes(int(sensor['cmdI2c']))

    def get_sensor_data_by_key(self, key):
        return self.i2c.readBytes(int(self.sensors[key]['cmdI2c']))
