import smbus as smbus

class I2CBus:    
    # for RPI version 1, use "bus = smbus.SMBus(0)"
    bus = smbus.SMBus(1)

    def __init__(self, address):
        self.address = address

    def readList(cmd):
        try:
            bytes = bus.read_i2c_block_data(self.address, cmd)
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
            return 'Error';