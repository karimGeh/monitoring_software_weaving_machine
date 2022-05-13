import time
import serial


def identifyAddressInPort(COM: str) -> int:
    ser = serial.Serial(COM, 9600)
    ser.close()
    ser.open()
    while not ser.inWaiting():
        time.sleep(0.5)

    address = int(ser.readline().decode())

    ser.close()
    return address
