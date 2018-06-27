# -*- coding: utf-8 -*-
import logging

from RobotConfig import RobotConfig
from Threads.ActualizeThread import ActualizeThread
from SocketServer.Server import SocketServerThread

class RobotApp:

    def start(self):
        self.logger = logging.getLogger(__name__)
        self.robotConfig = RobotConfig()        

        #PARA PRUEBAS EN WINDOWS SIN THREADS
        #thread = ActualizeThread(self.robotConfig)
        #thread.run()
        self._startActualizeThread()

        self._startSocketServer()

    def _startActualizeThread(self):
        newthread = ActualizeThread(self.robotConfig)
        newthread.start()

    def _startSocketServer(self):
        newthread = SocketServerThread(self.robotConfig)
        newthread.start()
