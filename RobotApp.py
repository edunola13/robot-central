# -*- coding: utf-8 -*-
from DeviceDrivers.SensorDriver import SensorDriver
from RobotConfig import RobotConfig
from Threads.ActualizeThread import ActualizeThread

class RobotApp:

    def start(self):        
        self.robotConfig = RobotConfig()

        thread = ActualizeThread(self.robotConfig)
        thread.run()

    #def startActualizeThread(self):
    #    newthread = ActualizeThread(self.config)
    #    newthread.start()