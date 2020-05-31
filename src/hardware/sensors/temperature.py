import adafruit_dht
import board

dhtDevice = adafruit_dht.DHT22(board.D4)


def get_temperature_from_sensor():
    return dhtDevice.temperature
