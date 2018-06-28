#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import logging.config
import signal
import sys
if sys.platform == 'win32':
    from signal import signal, SIGTERM
else:
    from signal import signal, SIGTERM, SIGHUP, SIGQUIT, SIGKILL
    #signal(SIGPIPE,SIG_DFL)

from RobotApp import RobotApp

root = os.path.dirname(os.path.abspath(__file__))
logging.config.fileConfig(root+'/logging.ini')
logger = logging.getLogger('service')

#
#NO FUNCIONA LO DE APAGADO
#
def handler(signum=None, frame=None):
    quit()
"""
if sys.platform == 'win32':
    for sig in [SIGTERM]:
        signal(sig, handler)
else:
    for sig in [SIGTERM, SIGHUP, SIGQUIT, SIGKILL]:
        signal(sig, handler)
"""

if __name__ == "__main__":
    logger.info("Starting Service")
    app = RobotApp()
    app.start()
