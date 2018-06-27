# -*- coding: utf-8 -*-
import socket, threading
import time
import importlib
import configparser

class SocketServerThread(threading.Thread):
    def __init__(self, robotConfig):
        threading.Thread.__init__(self)
        self.robotConfig = robotConfig
        self.config = self.robotConfig.get_section('Server-Socket')

    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((self.config.IP_SOCKET, self.config.PORT_SOCKET))
        server.listen(5)
        print("Server started")
        print("Waiting for client request..")
        while True:   
            clientsock, clientAddress = server.accept()
            newthread = SocketClientThread(clientAddress, clientsock)
            newthread.start()


class SocketClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        print ("New connection added: ", clientAddress)

    def run(self):
        print ("Connection from : ", clientAddress)
        msg = ''
        controller = null
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()

            if msg == 'exit':
                break

            if msg == 'controller':
                self.csocket.send(bytes('Indique el Controlador','UTF-8'))
                data = self.csocket.recv(2048)

                #ACA BUSCO LA CLASE DESDE EL CONFIG.INI
                className = self.config[data]['CLASS']
                libraryName = "Controllers"
                controllerModule = importlib.import_module(libraryName)
                controllerClass = getattr(controllerModule, className)
                
                controller = controllerClass()

                self.csocket.send(bytes('Controlador Listo','UTF-8'))
                continue
            
            #Le paso la data al controlador correspondiente
            rta = controller.serve(data)
            self.csocket.send(bytes(rta, 'UTF-8'))
            
        #Es como que cierra la conexion el cliente
        print ("Client at ", clientAddress , " disconnected...")