from time import sleep
from machine import ADC

class LDR:
  def __init__(self, dataPin):
    self.sensor = ADC(dataPin)
    self.MIN_LIGHT = 65535 
    self.MAX_LIGHT = 0

  def measure(self):
    light = self.__lightInPercentage(self.sensor.read_u16())
    return light

  def __lightInPercentage(self, value):
    light = round((self.MIN_LIGHT - value) * 100 / (self.MIN_LIGHT - self.MAX_LIGHT))
    return max(0, min(light, 100))