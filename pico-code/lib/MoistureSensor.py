from time import sleep
from machine import ADC
from machine import Pin

class MoistureSensor:
  def __init__(self, dataPin, pwrPin):
    self.sensor = ADC(dataPin)
    self.pwrPin = Pin(pwrPin, Pin.OUT)
    self.MIN_MOISTURE = 63000 # Dry soil
    self.MAX_MOISTURE = 40000 # Just watered soil

  def turnOn(self):
    self.pwrPin.value(1)
    sleep(0.5) # Pause program to make sure sensor is activated
  
  def turnOff(self):
    self.pwrPin.value(0)
     
  def readMoisture(self):
    self.turnOn() 
    value = self.sensor.read_u16()
    moisture = self.__moistureInPercentage(value)
    self.turnOff()
    
    #print("RAW moisture level is {}".format(value)) # Use this value to calibrate sensor
    return moisture

  def __moistureInPercentage(self, value):
    moisture = round((self.MIN_MOISTURE - value) * 100 / (self.MIN_MOISTURE - self.MAX_MOISTURE))
    return max(0, min(moisture, 100))