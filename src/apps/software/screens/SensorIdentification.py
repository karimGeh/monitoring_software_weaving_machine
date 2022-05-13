from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

from router import Screens
from config.machine import SENSORS, PORTS
from utils.Identify import identifyAddressInPort


class SensorIdentification(QWidget):
    def __init__(self, master):
        super(SensorIdentification, self).__init__()
        self.master = master
        loadUi("./src/apps/software/ui/sensorIdentification.ui", self)

        self.continueButton.clicked.connect(self.handleContinue)

        self.identificationDict = {}

        self.identified = 0
        self.numberOfSensors = len(SENSORS)

        self.identify()

    def identify(self):
        for port in PORTS:
            address = identifyAddressInPort(port)
            self.identificationDict[address] = port
            self.identified += 1
            self.update()

    def update(self):
        self.identificationLabel.setText(
            f"{self.identified} / {self.numberOfSensors} sensor identified"
        )
        self.identificationProgressBar.setValue(
            self.identified * 100 / self.numberOfSensors
        )

    def handleContinue(self):
        print(self.identificationDict)
        if self.identified != self.numberOfSensors:
            return

        self.master.goTo(Screens.MonitoringScreen)
