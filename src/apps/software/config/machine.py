from lib.Sensor import Sensor

PORTS = [
    "COM4"
]

SENSORS = [
    # this is a test sensor
    Sensor(
        name="test_sensor",
        address=0,
        file_location="./src/apps/software/db/test_sensor.csv",
        columns_name=["TIME", "VALUE"],
    )
]
