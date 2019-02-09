#!/bin/env python3

import RPi.GPIO as GPIO
import time

#Initialization
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Define GPIO18 as exit
GPIO.setup(18,GPIO.OUT)


#Turn GPIO18 ON
GPIO.output(18,GPIO.HIGH)
#Wait one second
time.sleep(1)
#Turn GPIO18 OFF
GPIO.output(18,GPIO.LOW)


