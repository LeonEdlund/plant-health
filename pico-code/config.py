# Configuration file
# Update these values with your credentials and specific values.

import ubinascii
from machine import unique_id

# WiFi
WIFI_SSID = 'CHANGE_ME' # Replace with your WIFI name
WIFI_PASS = 'CHANGE_ME' # Replace with your WIFI password

# MQTT CREDENTIALS
MQTT_SERVER = 'CHANGE_ME' # Replace with your server
MQTT_PORT = 1883 # Replace if you've change the default port 
MQTT_USER = 'CHANGE_ME' # Replace with your MQTT Username
MQTT_KEY = 'CHANGE_ME' # Replace with your MQTT password
MQTT_TOPIC = 'CHANGE_ME' # Replace with the MQTT topic name
MQTT_CLIENT_ID = ubinascii.hexlify(unique_id()) # A unique string to use as client id 

# APPLICATION LOGIC OPTIONS
MOISTURE_THRESHOLD = 30 # Change this to adjust at what moisture level (%) the LED should turn on at
TIME_BETWEEN_MEASUREMENTS = 15 # Change this to set how often (in seconds) the sensors should read data.  