import Adafruit_DHT


def get_dht22_data(pin):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pin)
    return humidity, temperature
