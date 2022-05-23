import sys
import time
import typing
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication

import _thread

from App import App
from config.machine import PORTS
from lib.SensorListener import SensorListener
from config.machine import SENSORS

# import resources

app = QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon("src/favicon.png"))

widget = App()
widget.show()

sensorListeners: typing.List[SensorListener] = []
for port in PORTS:
    sensorListeners += [SensorListener(port)]


def readListenersData():
    while 1:
        for listener in sensorListeners:
            listener.readData()
        # time.sleep(0.1)


widget.sensorListeners = sensorListeners
_thread.start_new_thread(readListenersData, ())


try:
    sys.exit(app.exec_())
except:
    print("Exiting")
