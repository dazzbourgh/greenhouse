import Adafruit_DHT


def get_temperature_from_sensor():
    _, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    return temperature
