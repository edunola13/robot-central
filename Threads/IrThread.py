# -*- coding: utf-8 -*-
import logging
import threading
import time

#from DeviceDrivers.SensorDriver import SensorDriver

class IrThread(threading.Thread):
    def __init__(self, robotConfig, device):
        threading.Thread.__init__(self)
        self.logger = logging.getLogger(__name__)
        self.robotConfig = robotConfig
        if (self.robotConfig.exists_section(device)):
            self.device = self.robotConfig.get_section(device)
        else:
            self.logger.error('El dispositivo IR ' + device + ' no existe en la configuracion');        

    def run(self):
        if (self.device):
            while True:
                None
                #ACA ESPERO COMUNICACION SERIAL A TRAVES DEL DRIVER CORRESPONDIENTE

        self.logger.info('El thread IR se termino por falta de configuracion');
