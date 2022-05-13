from lib.Sensor import Sensor

PORTS = ["COM3", "COM4"]

SENSORS = [
    # this is a test sensor
    Sensor(
        name="test_sensor_1",
        address=1,
        file_location="./src/apps/software/db/test_sensor1.csv",
        columns_name=["TIME", "VALUE"],
    ),
    Sensor(
        name="test_sensor_2",
        address=2,
        file_location="./src/apps/software/db/test_sensor2.csv",
        columns_name=["TIME", "VALUE"],
    ),
]
