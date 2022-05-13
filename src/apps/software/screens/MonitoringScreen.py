from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFileDialog, QWidget
import pyqtgraph as pg
import numpy as np


class MonitoringScreen(QWidget):
  def __init__(self, master):
    super(MonitoringScreen, self).__init__()
    self.master = master
    loadUi("./src/apps/software/ui/monitoringScreen.ui", self)

    x = np.random.normal(size=1000)
    y = np.random.normal(size=1000)
