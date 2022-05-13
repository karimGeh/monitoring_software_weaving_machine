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
        self.identifyButton.clicked.connect(self.identify)

        self.identificationDict = {}

        self.identified = 0
        self.numberOfSensors = len(SENSORS)
        self.update()

    def identify(self):
        self.identified = 0
        self.identificationDict = {}
        for port in PORTS:
            address = identifyAddressInPort(port)
            self.identificationDict[address] = port
            self.identified += 1
            self.update()

    def update(self):
        self.identificationLabel.setText(
            f"""
                <html>
                    <head/>
                    <body>
                        <p align="center">
                            <span style=" font-size:14pt;">
                            {self.identified} / {self.numberOfSensors} sensor identified
                            </span>
                        </p>
                    </body>
                </html>
            """
            # f"{self.identified} / {self.numberOfSensors} sensor identified"
        )
        self.identificationProgressBar.setValue(
            self.identified * 100 / self.numberOfSensors
        )

    def handleContinue(self):
        print(self.identificationDict)
        if self.identified != self.numberOfSensors:
            return

        self.master.goTo(Screens.MonitoringScreen)
