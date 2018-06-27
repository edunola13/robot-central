# -*- coding: utf-8 -*-

import threading
import smbus as smbus
import time

class SensorsThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

    def run(self):
        while True:
            time.sleep(10)
            #Solicito datos por I2C