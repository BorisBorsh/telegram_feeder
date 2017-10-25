import Adafruit_DHT

def get_temp_message():
    """Return temperature and humidity message."""
    sensor = Adafruit_DHT.DHT11
    # Connected to GPIO23(16 BOARD).
    DHT_PIN_BOARD_NUMBER = 23
    humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT_PIN_BOARD_NUMBER)
    
    if not humidity and not temperature:
        return 'Failed to get tempereture reading.'

    return 'Temperature - {}C\nHumidity - {}%'.format(str(temperature), str(humidity))

