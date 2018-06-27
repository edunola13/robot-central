#import threading
import time

from DeviceDrivers.SensorDriver import SensorDriver

#class ActualizeThread(threading.Thread):
class ActualizeThread():
    def __init__(self, robotConfig):
        #threading.Thread.__init__(self)
        self.robotConfig = robotConfig

    def run(self):
        #while True:
        for section in self.robotConfig.sensors:
            dataSection = self.robotConfig.get_section(section)
            driver = SensorDriver(dataSection)
            driver.actualize_sensors()
            
            #time.sleep(int(self.robotConfig.config['Thread-Actualize']['SLEEP_TIME']))