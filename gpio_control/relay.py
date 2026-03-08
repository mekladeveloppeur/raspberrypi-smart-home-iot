import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LIGHT = 18
FAN = 23
BUZZER = 24

GPIO.setup(LIGHT, GPIO.OUT)
GPIO.setup(FAN, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)


def light_on():
    GPIO.output(LIGHT, 1)

def light_off():
    GPIO.output(LIGHT, 0)


def fan_on():
    GPIO.output(FAN, 1)

def fan_off():
    GPIO.output(FAN, 0)


def buzzer_on():
    GPIO.output(BUZZER, 1)

def buzzer_off():
    GPIO.output(BUZZER, 0)
