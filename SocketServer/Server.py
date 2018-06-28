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
        server.bind((self.config["IP_SOCKET"], int(self.config["PORT_SOCKET"])))
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
        self.clientAddress = clientAddress
        self.config = configparser.ConfigParser()
        self.config.read('SocketServer/config.ini')
        print ("New connection added: ", clientAddress)

    def run(self):
        msg = ''
        controller = None
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode().strip("\n")
            print ("Atendiendo")

            if msg == 'exit' or msg == '':
                break

            if msg == 'controller':
                self.csocket.send(bytes('Indique el Controlador','UTF-8'))
                data = self.csocket.recv(2048)
                msg = data.decode().strip("\n")

                #ACA BUSCO LA CLASE DESDE EL CONFIG.INI
                className = self.config[msg]['CLASS']
                libraryName = "SocketServer.Controllers"
                controllerModule = importlib.import_module(libraryName)
                controllerClass = getattr(controllerModule, className)
                
                controller = controllerClass()

                self.csocket.send(bytes('Controlador Listo','UTF-8'))
                continue

            if msg != '' and controller is not None:
                #Le paso la data al controlador correspondiente
                rta = controller.serve(msg)
                self.csocket.send(bytes(rta, 'UTF-8'))
            
        #Es como que cierra la conexion el cliente
        self.csocket.close()
        print ("Client at ", self.clientAddress , " disconnected...")
