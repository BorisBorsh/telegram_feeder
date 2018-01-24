try:
    import Adafruit_DHT
except ImportError:
    print('Adafruit_DHT import error.')


def get_tempereture_message():
    """Return temperature and humidity message."""
    try:
        sensor = Adafruit_DHT.DHT11
    except:
        return 'Failed to get tempereture. Adafruit module error.'

    # Connected to GPIO23(16 BOARD).
    DHT_PIN_BOARD_NUMBER = 23
    humidity, temperature = Adafruit_DHT.read_retry(sensor,
                                                   DHT_PIN_BOARD_NUMBER)

    if not humidity and not temperature:
        return 'Failed to get tempereture reading.'

    return 'Temperature - {}C\nHumidity - {}%'.format(temperature,
                                                      humidity)

