import RPi.GPIO as GPIO

from time import sleep


SERVO_PIN_BOARD_NUMBER = 11


class Servo:
    """Define a context menager Servo"""
    def __init__(self, SERVO_PIN_BOARD_NUMBER):
        self.SERVO_PIN_BOARD_NUMBER = SERVO_PIN_BOARD_NUMBER

    def __enter__(self):
        # Set up GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SERVO_PIN_BOARD_NUMBER, GPIO.OUT)

    def __exit__(self, type, value, tracebac):
        # Clean all GPIO pins settings
        GPIO.cleanup()


def servo_rotate(servo_rotate_time_sec=3):
    """Rotate servo to dispence food"""
    PWM_FREQ_HZ = 50
    PWM_START_DUTY_CYCLE = 0
    PWM_ROTATE_DUTY_CYCLE = 3
    
    # Start pulse width modulation
    pwm = GPIO.PWM(SERVO_PIN_BOARD_NUMBER, PWM_FREQ_HZ)
    pwm.start(PWM_START_DUTY_CYCLE)
    
    # Rorate servo
    pwm.ChangeDutyCycle(PWM_ROTATE_DUTY_CYCLE)
    sleep(servo_rotate_time_sec)
    pwm.stop()
    print('A portion of food was added.')


def feed_pet():
    """Controlling servo to feed pets"""
    with Servo(SERVO_PIN_BOARD_NUMBER):
        servo_rotate()


