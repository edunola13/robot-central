# -*- coding: utf-8 -*-
import json
from RobotConfig import RobotConfig
from DeviceDrivers.SensorDriver import SensorDriver

class SensorController:

    def __init__(self):
        self.robotConfig = RobotConfig()

    def serve(self, data):
        #DECODIFICO LA INFORMACION Y RETORNO LA INFORMACION DEL SENSOR CORRESPONDIENTE

        data = json.loads(data)

        if self.robotConfig.exists_section(data['device']):
            deviceConfig = self.robotConfig.get_section(data['device'])
            driver = SensorDriver(deviceConfig)
            rta = driver.get_sensor_data_by_key(data['sensor'])
            return rta

        return 'Error'
