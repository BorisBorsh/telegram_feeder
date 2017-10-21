import RPi.GPIO as GPIO
import Adafruit_DHT

from collections import deque
from time import sleep
from datetime import datetime


#def log_feeding_time(feed_time):
#    """Logging feeding time to console."""
#    message = feed_time + ' - Feeder fed a pet!'
#
#    try:
#        with open(filename, 'a') as f:
#            f.write('\n' + message)
#    except FileNotFoundError:
#        print('File not found!')
#    print(message)


def get_time():
    """Return current time."""
    now = datetime.today()
    return now.strftime('%H:%M')


def get_date_time():
    """Return current date and time."""
    now = datetime.today()
    return now.strftime('%Y-%m-%d %H:%M')


def get_temp():
    """Return temperature and humidity."""
    sensor = Adafruit_DHT.DHT11
    # Connected to GPIO23(16 BOARD).
    pin = 23
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        temp_message = ('Temperature - ' + str(temperature) +
                        'C\nHumidity - ' + str(humidity) + '%.')
    else:
        temp_message = 'Failed to get reading. Try again!'
    return temp_message


def show_log():
    """Show the last 10 feeding timings from log."""
    with open(filename) as f:
        last_timings = list(deque(f, 10))
        last_timings_message = ''
        for line in last_timings:
            last_timings_message += line
        return last_timings_message
