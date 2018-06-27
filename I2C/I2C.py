import smbus as smbus

class I2CBus:    
    # for RPI version 1, use "bus = smbus.SMBus(0)"
    bus = smbus.SMBus(1)

    def __init__(self, address):
        self.address = address

    def readBytes(self, cmd, retries = 5):
        try:
            bytes = self.bus.read_i2c_block_data(self.address, cmd)
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
            retries -= 1
            if retries > 0:
                self.readBytes(cmd, retries)
            else:
                return 'Error';

    def writeBytes(bytes, cmd, retries = 5):
        try:
            bus.write_i2c_block_data(self.address, cmd, bytes)
            return -1
        except Exception as e:
            print (e)
            retries -= 1
            if retries > 0:
                self.writeBytes(bytes, cmd, retries)
            else:
                return 'Error';
