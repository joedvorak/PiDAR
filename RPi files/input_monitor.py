#!/usr/bin/env python3

import RPi.GPIO as GPIO
from signal import pause
import os

inputPin = 4
def buttonPressed(channel):
    print("Input Received")
    os.system("python /home/pi/code/sweep/record_scan.py")
    

GPIO.setmode(GPIO.BCM)
GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(inputPin, GPIO.RISING, callback=buttonPressed, bouncetime = 2000)
pause()