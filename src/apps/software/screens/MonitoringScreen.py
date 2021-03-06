from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets

import pandas as pd
from config.machine import SENSORS_DICT

from utils.MplCanvas import MplCanvas

# from matplotlib.backends.backend_qt5agg import (
#     NavigationToolbar2QT as NavigationToolbar,
# )

# import matplotlib
# import numpy as np
# import random


SENSOR_TO_WIDGET = {
    "lcd_rapportTransmissionReel": 1,
    "graph": 2,
}


class MonitoringScreen(QWidget):
    def __init__(self, master):
        super(MonitoringScreen, self).__init__()
        self.master = master
        loadUi("./src/apps/software/ui/monitoringScreen.ui", self)

        # !!!! initialize plot - start
        self.mpl_canvas = MplCanvas(self, interval=100, updateFunc=self.drawLine)

        layout = QtWidgets.QVBoxLayout()

        # ? if we need to add toolbar
        # toolbar = NavigationToolbar(self.mpl_canvas, self)
        # layout.addWidget(toolbar)
        layout.addWidget(self.mpl_canvas)

        self.graphWrapper.setLayout(layout)
        self.show()
        # !!!! initialize plot - end

        # self._ref = 100
        self._x = []
        self._y = []
        self._i = 0
        self.maxPoints = 50

        for _ in range(self.maxPoints):
            self.readLastValues()

        self.startButton.clicked.connect(self.startMotor)
        self.stopButton.clicked.connect(self.stopMotor)

    def getSensorListenerByAddr(self, addr: int):
        i = -1
        for sensorListener in self.master.sensorListeners:
            i += 1
            if sensorListener.addr == addr:
                return sensorListener

    def startMotor(self):
        sensorListener = self.getSensorListenerByAddr(SENSOR_TO_WIDGET["graph"])
        sensorListener.writeData(b"1")
        print("start")

    def stopMotor(self):
        sensorListener = self.getSensorListenerByAddr(SENSOR_TO_WIDGET["graph"])
        sensorListener.writeData(b"0")
        print("stop")

    def readLastValues(self):
        sensor = SENSORS_DICT[SENSOR_TO_WIDGET["graph"]]
        data = pd.read_csv(sensor.file_location)

        self._x = data[sensor.columns_name[0]]
        self._y = data[sensor.columns_name[1]]

        # if self._i >= self.maxPoints:
        self._x = self._x[-self.maxPoints :]
        self._y = self._y[-self.maxPoints :]

    def readLcdValues(self):
        sensor = SENSORS_DICT[SENSOR_TO_WIDGET["lcd_rapportTransmissionReel"]]
        data = pd.read_csv(sensor.file_location)
        values = data[sensor.columns_name[1]].values
        longeur_tisser = data[sensor.columns_name[2]].values
        if len(values) == 0 or len(longeur_tisser) == 0:
            return

        # print(values)
        self.lcd_rapportTransmissionReel.display(values[-1])
        self.lcd_longeurTisser.display(longeur_tisser[-1])

    def drawLine(self):
        self.readLastValues()
        self.readLcdValues()
        self.mpl_canvas.fig.clf()
        ax = self.mpl_canvas.fig.subplots(1)
        ax.clear()
        ax.plot(self._x, self._y)
        ax.set_ylim(0, max([*self._y, 0]) + 100)
        self.mpl_canvas.fig.canvas.draw()

    def __repr__(self) -> str:
        # return super().__repr__()
        return "monitoring screen ..."
