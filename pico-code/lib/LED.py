from machine import Pin 
from time import sleep

class LED:
    def __init__(self, powerPin):
        self.led = Pin(powerPin, Pin.OUT)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)

    def blink(self, nrOfBlinks, speed):
        count = 0

        while count < nrOfBlinks * 2:
            count += 1
            self.led.toggle()
            sleep(speed)