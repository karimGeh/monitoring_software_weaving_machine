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
        self.values = {name: [] for name in columns_name}

        self.wipeFile()
        self.startWritting = False

    def wipeFile(self):
        with open(self.file_location, "w") as f:
            csvWriter = csv.DictWriter(f, fieldnames=self.columns_name)
            csvWriter.writeheader()

    def writeLine(self, values: typing.List[float]):
        if not self.startWritting and values[0] < 500:
            self.startWritting = True
        if not self.startWritting:
            return

        # values[0] = f"{}:"
        with open(self.file_location, "a") as f:
            csvWriter = csv.DictWriter(f, fieldnames=self.columns_name)
            info = {key: value for key, value in zip(self.columns_name, values)}
            csvWriter.writerow(info)
