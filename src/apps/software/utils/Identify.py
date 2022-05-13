import time
import serial


def identifyAddressInPort(COM: str) -> int:
    ser = serial.Serial(COM, 9600)
    ser.close()
    ser.open()
    while True:
        time.sleep(0.5)

        if not ser.inWaiting():
            continue

        try:
            address = ser.readline().decode()
            print(address)
            address = int(address)

            ser.close()
            return address
        except:
            continue
