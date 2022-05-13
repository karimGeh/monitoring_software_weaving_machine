import csv
import typing


class Sensor:
    def __init__(
        self,
        name: str,
        address: int,
        file_location: str,
        columns_name: typing.List[str],
    ) -> None:
        self.name = name
        self.address = address
        self.file_location = file_location
        self.columns_name = columns_name

    def wipeFile(self):
        with open(self.file_location, "w") as f:
            csvWriter = csv.DictWriter(f, fieldnames=self.columns_name)
            csvWriter.writeheader()

    def writeLine(self, values: typing.List[float]):
        with open(self.file_location, "a") as f:
            csvWriter = csv.DictWriter(f, fieldnames=self.columns_name)
            info = {key: value for key, value in zip(self.columns_name, values)}
            csvWriter.writerow(info)
