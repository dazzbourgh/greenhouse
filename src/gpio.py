import time

import RPi.GPIO as GPIO

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, True)
    time.sleep(3)
    GPIO.output(11, False)
    GPIO.cleanup()
