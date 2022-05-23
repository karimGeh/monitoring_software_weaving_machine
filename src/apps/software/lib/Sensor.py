import csv
import typing


class Sensor:
    def __init__(
        self,
        name: str,
        address: int,
        file_location: str,
        columns_name: typing.List[str],
        is_cmd=True,
        is_read=True,
    ) -> None:
        self.name = name
        self.address = address
        self.file_location = file_location
        self.columns_name = columns_name
        self.values = {name: [] for name in columns_name}
        self.is_cmd = is_cmd
        self.is_read = is_read

        self.wipeFile()
        self.startWriting = False

    def wipeFile(self):
        if not self.is_read:
            return
        with open(self.file_location, "w") as f:
            csvWriter = csv.DictWriter(f, fieldnames=self.columns_name)
            csvWriter.writeheader()

    def writeLine(self, values: typing.List[float]):
        if not self.is_read:
            return

        # if not self.startWriting and values[0] < 500:
        #     self.startWriting = True
        # if not self.startWriting:
        #     return

        # values[0] = f"{}:"
        with open(self.file_location, "a") as f:
            csvWriter = csv.DictWriter(f, fieldnames=self.columns_name)
            info = {key: value for key, value in zip(self.columns_name, values)}
            csvWriter.writerow(info)

    def printLine(self, line: str):
        if not self.is_cmd:
            return
        self.ser(line)
