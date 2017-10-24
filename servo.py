import RPi.GPIO as GPIO
import logging
import logging.config

from time import sleep


logging.config.fileConfig('logging.config')

logger = logging.getLogger('servoLogger')


class ServoContext:
    """Define a context menager Servo"""
    def __init__(self, SERVO_PIN_BOARD_NUMBER):
        self.SERVO_PIN_BOARD_NUMBER = SERVO_PIN_BOARD_NUMBER

    def __enter__(self):
        # Set up GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.SERVO_PIN_BOARD_NUMBER, GPIO.OUT)

    def __exit__(self, type, value, tracebac):
        # Clean all GPIO pins settings
        GPIO.cleanup()


def servo_rotate(SERVO_ROTATE_TIME_SEC, SERVO_PIN_BOARD_NUMBER):
    """Rotate servo to dispence food"""
    PWM_FREQ_HZ = 50
    PWM_START_DUTY_CYCLE = 0
    PWM_ROTATE_DUTY_CYCLE = 3
    
    # Start pulse width modulation
    pwm = GPIO.PWM(SERVO_PIN_BOARD_NUMBER, PWM_FREQ_HZ)
    pwm.start(PWM_START_DUTY_CYCLE)
    
    # Rorate servo
    pwm.ChangeDutyCycle(PWM_ROTATE_DUTY_CYCLE)
    sleep(SERVO_ROTATE_TIME_SEC)
    pwm.stop()
    print('A portion of food was added.')


def feed_pet(SERVO_ROTATE_TIME_SEC=3):
    SERVO_PIN_BOARD_NUMBER = 11
    """Controlling servo to feed pets"""
    with ServoContext(SERVO_PIN_BOARD_NUMBER):
        servo_rotate(SERVO_ROTATE_TIME_SEC, SERVO_PIN_BOARD_NUMBER)
        logger.info('- Fed pet.')
