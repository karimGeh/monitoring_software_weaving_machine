import serial
from config.machine import SENSORS_DICT


class SensorListener:
    def __init__(self, port) -> None:
        self.port = port
        self.ser = serial.Serial(port, 9600)
        self.ser.close()
        self.ser.open()
        i = 0
        while self.ser.inWaiting() and i < 20:
            self.ser.readline().decode().split(",")
            i += 1

    def readData(self):
        try:
            if self.ser.inWaiting():
                addr, *data = self.ser.readline().decode().split(",")

                addr = int(addr)
                (*values,) = map(float, data)

                if addr not in SENSORS_DICT:
                    return

                SENSORS_DICT[addr].writeLine(values)
        except:
            pass
