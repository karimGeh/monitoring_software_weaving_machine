from enum import Enum
from PyQt5 import QtGui, QtWidgets

# !
from utils.InnerWidget import InnerWidget

# ! widgets
from screens.MonitoringScreen import MonitoringScreen
from screens.SensorIdentification import SensorIdentification

# ! pages
from router import Screens

# ! configs
from config.software import WINDOW_HEIGHT, WINDOW_WIDTH, WINDOW_TITLE


class App(QtWidgets.QStackedWidget):
    def __init__(self) -> None:
        super(App, self).__init__()

        self.pages = {
            # Screens.SensorIdentification: InnerWidget(self, SensorIdentification),
            Screens.MonitoringScreen: InnerWidget(self, MonitoringScreen),
        }

        self.initialScreen = Screens.MonitoringScreen

        for value in self.pages.values():
            self.addWidget(value.innerWidget)

        self.setWindowTitle(WINDOW_TITLE)
        self.setFixedHeight(WINDOW_HEIGHT)
        self.setFixedWidth(WINDOW_WIDTH)
        self.setCurrentIndex(self.pages[self.initialScreen].index)

    def startIdentification(self):
        self.pages[Screens.SensorIdentification].innerWidget.identify()

    def goTo(self, page):
        if page not in self.pages:
            raise Exception("page not found")

        self.setCurrentIndex(self.pages[page].index)
