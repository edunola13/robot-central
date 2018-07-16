# -*- coding: utf-8 -*-
import logging
import threading
import time

from DeviceDrivers.SensorDriver import SensorDriver

class ActualizeThread(threading.Thread):
    def __init__(self, robotConfig):
        threading.Thread.__init__(self)
        self.robotConfig = robotConfig
        self.logger = logging.getLogger(__name__)

    def run(self):
        while True:
            self.logger.info('Actualizando los Sensores')
            for section in self.robotConfig.sensors:
                dataSection = self.robotConfig.get_section(section)
                driver = SensorDriver(dataSection)
                driver.actualize_sensors()
            
            time.sleep(int(self.robotConfig.config['Thread-Actualize']['SLEEP_TIME']))