import RPi.GPIO as GPIO

MQ2 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(MQ2, GPIO.IN)


def gas_detect():

    if GPIO.input(MQ2):
        return False
    else:
        return True
