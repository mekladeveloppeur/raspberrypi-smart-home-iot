import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4


def read_dht():

    humidity, temperature = Adafruit_DHT.read(sensor, pin)

    if humidity is not None:
        return temperature, humidity

    return None, None
