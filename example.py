#!/usr/bin/env python
# coding=utf-8

# [pi] byte = bus.read_byte(address) -> [arduino] Wire.onRequest(handler)
 
import smbus as smbus
import time
import sys

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)
 
address = 0x04
 
def readNumber():
    try:
        number = bus.read_byte(address)
        return number
    except:
        return 99999;

def readList():
    try:
        bytes = bus.read_i2c_block_data(address, 2)
        print (len(bytes))
        print (bytes)
        data = ""
        for byte in bytes:
            if byte == 255 :
                break
            data += chr(byte)
        return data
    except Exception as e:
        print (e)
        return 99999;

def writeNumber(value):
    try:
        bus.write_byte(address, value)
        return -1
    except:
        print ("error")

def writeBytes(bytes):
    try:
        bus.write_i2c_block_data(address, 0, bytes)
        return -1
    except:
        print ("error 1")
 
while True: 
    time.sleep(3)
    #number = readNumber()
    data = readList();
    print ("RPI recibiendo de Arduino: ", data)
    #print

    #var = int(input("Introduce un valor 1 - 9: "))
    #if not var:
    #    continue

    writeBytes([104, 61, 48])
    #writeNumber(var)
    #print ("Se envio dato")

    #sys.exit(1)


import socket, threading

class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)

    def run(self):
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=='bye':
              break
            print ("from client", msg)
            self.csocket.send(bytes(msg,'UTF-8'))
        #Es como que cierra la conexion el cliente
        print ("Client at ", clientAddress , " disconnected...")

LOCALHOST = "127.0.0.1"
PORT = 50001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
server.listen(5)
print("Server started")
print("Waiting for client request..")
while True:   
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()