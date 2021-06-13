#!/usr/bin/python
import RPi.GPIO as GPIO
import time
def getMoist():
    # GPIO SETUP
    channel = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)


    def callback(channel):
        if GPIO.input(channel):
            msg = "Water Needed!"
            return msg

        else:
            msg = "no water needed!"
            return msg


    GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
    GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

    # infinite loop
    while True:
        time.sleep(1)



