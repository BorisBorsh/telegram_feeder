import RPi.GPIO as GPIO
import logging
import logging.config

from time import sleep

logging.config.fileConfig('logging.config')
logger = logging.getLogger('servoLogger')

MOTOR_PIN_BOARD_NUMBER = 10
PORTIONS_COUNTER_SENSOR_PIN_BOARD_NUMBER = 18


class MotorContext:
    """Define a context maneger Motor"""
    def __init__(self):
        self.temporary_attribute = 12

    def __enter__(self):
        # Set up GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PORTIONS_COUNTER_SENSOR_PIN_BOARD_NUMBER, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(MOTOR_PIN_BOARD_NUMBER, GPIO.OUT)

    def __exit__(self, type, value, tracebac):
        # Clean all GPIO pins settings
        GPIO.cleanup()


def start_motor_rotation():
    """Starts motor rotation to dispence food. Motor is connected to
    raspbbery pi using a relay. This function controlling relay
    signal pin"""
    GPIO.output(MOTOR_PIN_BOARD_NUMBER, True)


def stop_motor_rotation():
    """Stops motor rotation"""
    GPIO.output(MOTOR_PIN_BOARD_NUMBER, False)


def check_current_position_of_portions_counter():
    """Counting dispenced portions of food. To avoid microswitch
    contact bounce it is neccesary to get while loop. Then detect when
    microswitch would break circle."""
    while GPIO.input(PORTIONS_COUNTER_SENSOR_PIN_BOARD_NUMBER) == 0:
        #print("microswitch is switched on.")
        sleep(0.7)


def dispence_food(portions_to_dispence=1):
    """Rotate motor to dispence food"""
    dispenced_portions_counter = 0

    with MotorContext():

        while dispenced_portions_counter < portions_to_dispence:

            start_motor_rotation()

            if GPIO.input(PORTIONS_COUNTER_SENSOR_PIN_BOARD_NUMBER) == 0:
                check_current_position_of_portions_counter()
                dispenced_portions_counter += 1
            sleep(.3)

        stop_motor_rotation()
        logger.info('- Fed pet.')


if __name__ == '__main__':
    dispence_food(portions_to_dispence=1)
