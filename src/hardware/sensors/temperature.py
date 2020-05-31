import adafruit_dht
import board

dhtDevice = adafruit_dht.DHT22(board.D18)


def get_temperature_from_sensor():
    return dhtDevice.temperature
