import config
import json
from time import sleep
from mqtt import MQTTClient
from machine import Pin
from MoistureSensor import MoistureSensor
from LDR import LDR
from dht import DHT11
from LED import LED

# Sensor setup
moistureSensor = MoistureSensor(dataPin=27, pwrPin=16)
ldr = LDR(dataPin=28)
thSensor = DHT11(Pin(26))
led = LED(0)

# Client connection
client = MQTTClient(config.MQTT_CLIENT_ID, config.MQTT_SERVER, config.MQTT_PORT, config.MQTT_USER, config.MQTT_KEY)
client.connect()

# Read all sensors
def readSensors():
    # Get moisture level
    moisture = moistureSensor.readMoisture()
        
    # Get temp and humidity
    thSensor.measure()
    temp = thSensor.temperature()
    humidity = thSensor.humidity()

    # Get light
    light = ldr.measure()

    # Save as dictionary 
    readings = {
        "moisture":moisture,
        "temp":temp,
        "humidity":humidity,
        "light":light}
    
    return readings

# Turn on led if moisture level is under defined threshold
def checkLEDStatus(moisture):
    if(moisture < config.MOISTURE_THRESHOLD):
        led.on()
    else:
        led.off()

# Print values to console
def printToConsole(data): 
    print("")
    print(f"Moisture: {data['moisture']}%")
    print(f"Temperature: {data['temp']} degrees Celsius")
    print(f"Room-Humidity: {data['humidity']}%")
    print(f"Light: {data['light']}%")
    print("")
    print("--------------------------------------")

# Main Program Loop 
while True:
    try:
        data = readSensors()
        checkLEDStatus(data['moisture'])
        client.publish(topic=config.MQTT_TOPIC, msg=json.dumps(data))
        printToConsole(data)
    except Exception as error:
        led.blink(nrOfBlinks=3, speed=0.5)
        print("Exception occurred", error)
    
    sleep(config.TIME_BETWEEN_MEASUREMENTS) # Time between each measurement