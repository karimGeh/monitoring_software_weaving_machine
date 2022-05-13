import time
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar,
)

import matplotlib
import numpy as np
import random

from utils.MplCanvas import MplCanvas


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

        self._ref = 100
        self._x = []
        self._y = []
        self._i = 0
        self.maxPoints = 100

        for _ in range(self.maxPoints):
            self.generateNewValue()

    def generateNewValue(self):
        self._ref = max(min(110, self._ref + random.randint(-3, 3)), 90)
        self._i += 1
        self._x += [self._i]
        self._y += [self._ref]
        if self._i >= self.maxPoints:
            self._x = self._x[-self.maxPoints :]
            self._y = self._y[-self.maxPoints :]

    def drawLine(self):
        self.generateNewValue()
        self.mpl_canvas.fig.clf()
        ax = self.mpl_canvas.fig.subplots(1)
        ax.clear()
        ax.plot(self._x, self._y)
        ax.set_ylim(0, max(self._y) + 100)
        self.mpl_canvas.fig.canvas.draw()

    def __repr__(self) -> str:
        # return super().__repr__()
        return "monitoring screen ..."
