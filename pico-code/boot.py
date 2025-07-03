import wifiConnect
from LED import LED 

# WiFi Connection
try:
    ip = wifiConnect.connect() 
except: 
    led = LED(0)
    led.blink(nrOfBlinks=5, speed=0.5)  # Blink the LED 5 times to show that something went wrong on boot