from lib.Sensor import Sensor

PORTS = [
    "COM5",
    "COM3",
]

SENSORS = [
    # this is a test sensor
    Sensor(
        name="capteur_glissement",
        address=1,
        file_location="./src/apps/software/db/capteur_glissement.csv",
        columns_name=["TIME", "RAPPORT_DE_TRANSMISSION"],
    ),
    Sensor(
        name="test_sensor_2",
        address=2,
        file_location="./src/apps/software/db/test_sensor2.csv",
        columns_name=["TIME", "VALUE"],
    ),
]

SENSORS_DICT = {sensor.address: sensor for sensor in SENSORS}
