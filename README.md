# Plant-Health: A plant monitoring IoT-device  

__Author:__ Leon Edlund 

__Student-ID:__ le223nd

__Time to complete:__ Around 4-6 hours

---

In this tutorial, we’ll create a small IoT device to monitor your plant’s health. This includes reading the _soil moisture, sun exposure, room temperature, and humidity_.  

The data gathered is presented using a self-hosted solution. A _TIG stack (Telegraf, InfluxDB, and Grafana)_ is used to store and visualize the data, all running inside Docker containers.  

Depending on your prior experience, this project should be fairly straightforward and should not take longer than a few hours to complete.  

Let’s get started!

## Objective

I recently got a new plant, which is very exciting. The only problem with this plant is that it needs to be watered very often. If I forget to water it, it quickly starts drooping and looks at me with its sad, disappointed petals, and I start feeling guilty. To avoid having to see my plant sad ever again, I created a device that can notify me when the plant needs water by turning on an LED light when the soil moisture is too low. I also receive a message on Discord telling me it's time to water.

While this was the main goal of the device, I also thought it would be fun to monitor some other aspects of the plant’s life to gain insight into how the surrounding environment affects its health and wellbeing, things like _room temperature, air humidity, and sun exposure._

So if you have a sad plant that needs a bit of extra supervision, this is the perfect project for you, and your plant will __thank you.__

## Material

So what do you need to create this?

I got this [IoT starter kit](https://www.electrokit.com/lnu-starter) from Electrokit, which includes most of the things you need, plus some extra sensors that are not used in this project. I also had to buy this [soil sensor](https://www.electrokit.com/lnu-starter) that was not included in the starter kit.

Overall, I spent around 400 SEK on this project. It will be slightly cheaper if you only want to buy the necessary components individually.

Below is a complete list of the materials:

<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Picture</th>
      <th>Link to buy</th>
      <th>Amount</th>
      <th>Price (SEK)</th>
      <th>Used for</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Raspberry Pi Pico WH</th>
      <td>
        <img src="https://www.electrokit.com/resource/u1sX/ZiO/SY7MHfFWQMg/product/41019/41019114/PICO-WH-HERO.jpg"/>
      </td>
      <td>
        <a href="https://www.electrokit.com/raspberry-pi-pico-wh">Link</a>
      </td>
      <td>1 pc</td>
      <td>99 SEK</td>
      <td>Microcontroller: the brains of the operation. Runs code and connects to Wi-Fi.</td>
    </tr>
    <tr>
      <th>Solderless Breadboard, 840 tie-points</th>
      <td>
        <img src="https://www.electrokit.com/upload/product/10160/10160840/10160840.jpg"/>
      </td>
      <td>
        <a href="https://www.electrokit.com/en/kopplingsdack-840-anslutningar">Link</a>
      </td>
      <td>1 pc</td>
      <td>69 SEK</td>
      <td>Used to connect everything without soldering.</td>
    </tr>
    <tr>
      <th>USB-cable A-male - micro B female 60cm </th>
      <td>
        <img src="https://media.rs-online.com/C1828496-01.jpg"/>
      </td>
      <td>
        <a href="https://www.electrokit.com/en/usb-kabel-a-hane-micro-b-hane-60cm">Link</a>
      </td>
      <td>1 pc</td>
      <td>28 SEK</td>
      <td>A usb cable to power the Pico.</td>
    </tr>
    <tr>
      <th>Wall Plug</th>
      <td>
        <img src="https://www.telefonshoppen.se/bilder/artiklar/apple-usb-power-adapter-5w.jpg"/>
      </td>
      <td>
      </td>
      <td>1 pc</td>
      <td>FREE</td>
      <td>A wall plug to power the pico. You probably already have one</td>
    </tr>
    <tr>
      <th>Soil hygrometer module</th>
      <td>
        <img src="https://www.electrokit.com/upload/product/41015/41015738/41015738.jpg"/>
      </td>
      <td>
        <a href="https://www.electrokit.com/en/jordfuktighetssensor">Link</a>
      </td>
      <td>1 pc</td>
      <td>29 SEK</td>
      <td>Used to measure soil moisture level.</td>
    </tr>
    <tr>
      <th>Digital temperature and humidity sensor (DHT11)</th>
      <td>
        <img src="https://www.electrokit.com/upload/product/41015/41015728/41015728.jpg"/>
      </td>
      <td>
        <a href="https://www.electrokit.com/en/digital-temperatur-och-fuktsensor-dht11">Link</a>
      </td>
      <td>1 pc</td>
      <td>49 SEK</td>
      <td>Used to measure room temperature and air humidity.</td>
    </tr>
    <tr>
      <th>Photoresistor CdS 4–7 kΩ</th>
      <td>
        <img src="https://www.electrokit.com/upload/product/40850/40850001/40850001.jpg"/>
      </td>
      <td>
        <a href="https://www.electrokit.com/en/fotomotstand-cds-4-7-kohm">Link</a>
      </td>
      <td>1 pc</td>
      <td>9.50 SEK</td>
      <td>Used to measure light level.</td>
    </tr>
    <tr>
      <th>LED 5 mm red diffuse 1500 mcd</th>
      <td>
        <img src="https://www.electrokit.com/upload/product/40307/40307020/40300051.jpg"/>
      </td>
      <td>
        <a href="https://www.electrokit.com/en/led-5mm-rod-diffus-1500mcd">Link</a>
      </td>
      <td>1 pc</td>
      <td>5 SEK</td>
      <td>Used to notify when the plant needs water, and for user feedback if the device is unable to connect to Wi-Fi.</td>
    </tr>
    <tr>
      <th>Jumper wire cable 20-pin, 15 cm, Dupont male/male</th>
      <td>
        <img src="https://www.electrokit.com/upload/product/41012/41012909/41012909.jpg"/>
      </td>
      <td>
        <a href="https://www.electrokit.com/en/labbsladd-20-pin-15cm-hane/hane">Link</a>
      </td>
      <td>1 pc</td>
      <td>52 SEK</td>
      <td>Pack of wires to connect everything together.</td>
    </tr>
    <tr>
      <th>Resistor 1W 5% 220 Ω (220R)</th>
      <td>
        <img src="https://www.electrokit.com/resource/u2Yr/7Vt/Qv1oCvZfkHX/product/40812/40812016/40812016.png"/>
      </td>
      <td>
        <a href="https://www.electrokit.com/en/motstand-1w-5220ohm-220r">Link</a>
      </td>
      <td>1 pc</td>
      <td>2 SEK</td>
      <td>Resistor to protect the LED.</td>
    </tr>
    <tr>
      <th>Resistor 2W 4.7 kΩ 5% (4k7)</th>
      <td>
        <img src="https://www.electrokit.com/resource/uC3q/4dm/4tRgVIIJnJ/product/41011/41011678/41011678.png"/>
      </td>
      <td>
        <a href="https://www.electrokit.com/en/motstand-2w-4.7kohm-54k7">Link</a>
      </td>
      <td>1 pc</td>
      <td>3 SEK</td>
      <td>Resistor for the photoresistor.</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th colspan="5">Total Price:</th>
      <td>345.50 SEK</td>
    </tr>
  </tfoot>
</table>

## Computer setup

Once you have all the hardware, it's time to set up your development environment. I'm doing this on a Mac, but I assume the steps will be similar on Windows. If you're on Linux, you probably know what you're doing already.

### Step 0: Flash the Pico firmware

The first step is to flash the firmware on your Raspberry Pi Pico so it can run the code you write for it.

1. If you bought the one provided in the bill of materials, download this [firmware](https://micropython.org/resources/firmware/RPI_PICO_W-20250415-v1.25.0.uf2).

2. Once the file is downloaded, hold down the _BOOTSEL_ button on your Pico while you plug it into your computer with the USB cable. The Pico will now show up as a storage device on your computer.

3. Drag the downloaded firmware file onto the Pico.

4. Wait for the transfer to complete. The Pico will automatically flash the firmware and restart.

5. That's it! You now have the correct firmware installed.

### Step 1: Install Visual Studio Code

The next step is installing an IDE so you have somewhere to write your code.  
I'm using Visual Studio Code, since that is my preferred IDE and will therefore be the one used in this tutorial.

Download and install Visual Studio Code by following this [link](https://code.visualstudio.com/).

### Step 2: Install the PyMakr plugin

Once you've installed Visual Studio Code, you need to download the PyMakr plugin. This extension enables you to easily upload code and control your Pico microcontroller directly via Visual Studio Code, which makes development much easier.

Follow this [tutorial](https://docs.pycom.io/gettingstarted/software/vscode/) on how to download and install PyMakr.

_Note: You need Node.js installed for PyMakr to work, but it's all explained in the tutorial above._

### Step 3: Upload code to the Raspberry Pi Pico

Once you have PyMakr installed, you’re ready to upload the code to the Pico.  
_You may want to follow the __Putting Everything Together__ section before doing this step._

To get started, clone this repository. From within the `/pico-code` folder, create a new PyMakr project and upload the code to the Pico.

If you’d like a more detailed explanation of how to set up and use PyMakr, follow [this tutorial](https://embedded-systems-design.github.io/using-pymakr/).

## Putting everything together

![Wiring Diagram](/assets/wiring_diagram.png)

Above is a wiring diagram showing how to connect all the sensors to the Pico using the breadboard listed in the bill of materials.

_Note: This setup is meant for development. To tidy up the project and make it production-ready, soldering instead of using the breadboard would be necessary, and possibly 3D-printing a case._

As seen in the diagram, three sensors and one LED are used:

1. __Soil moisture sensor:__  
   To read the data from this sensor (_bottom right_), it is connected to one of the ADC pins (GP27) on the Pico. This allows us to convert the analog signal from the sensor into a digital value we can use in our code. To power the sensor, it is connected to its own GPIO pin (GP16). This allows us to independently turn the sensor on and off while taking a measurement. Ground is connected to the Pico’s GND pin, which is linked to the ground rail on the breadboard.

2. __Temperature and humidity sensor:__  
   This sensor (DHT11 — _far left_) is connected to GP26 for reading data. It is powered by the 3.3V pin via the power rail, and ground is connected to the ground rail.

3. __Photoresistor:__  
   This sensor is also connected to an ADC pin (GP28). It is powered by the 3.3V pin, and ground is connected to the ground rail. A 4.7 kΩ resistor is placed between the 3.3V power pin and the photoresistor to create a _voltage divider_. This setup converts the changing resistance of the photoresistor into a variable voltage the ADC can read.

4. __LED:__  
   The LED’s long leg (+) is connected to GP0 for power, and the short leg (-) is connected to ground. To prevent the LED from burning out due to too much current, a 220 Ω resistor is placed in the circuit.

## Platform

### Adafruit IO

At first, I used [Adafruit IO](https://adafruit.io), a cloud-based solution, to store and visualize data gathered by the device. This was very simple and straightforward, and it’s a great option if you don’t want to deal with self-hosting.  

If you prefer this route, you can follow these [beginner guides](https://learn.adafruit.com/series/adafruit-io-basics) to set up a feed and dashboard. Then all you need to do is adjust the Pico config file (`/pico-code/config.py`) with your Adafruit credentials. You should then be able to visualize your data relatively quickly.

### TIG Stack

While Adafruit IO was a good and simple solution, I wanted to have more freedom to customize the dashboard, better actions and the ability to scale the project without having to pay a subscription fee. I also found this to be a good opportunity to work with Docker for the first time.

Therefor a TIG stack (Telegraf, InfluxDB, Grafana) along with Mosquitto MQTT was used running inside a Docker containers and using Docker-compose to manage them. For now, this only runs locally on my machine, but since it’s containerized, it could be installed on a separate server as a more long-term solution.

The stack:

1. __Eclipse Mosquitto__: The MQTT broker responsible for receiving and forwarding information sent via the MQTT protocol from the device.

2. __Telegraf__: Collects the data from the MQTT broker and pushes it to InfluxDB.

3. __InfluxDB__: A time-series database used to store the data from the device.

4. __Grafana__: An open-source data visualization tool used to create dashboards and display the data stored in InfluxDB.

To set up the same Docker config as me see `README.md` in `/docker-tig-stack` 

# The Code

### Get up and running

The code for the Pico (`pico-code`) is pretty straightforward. To get started, all you have to do is adjust the `config.py` file with your Wi-Fi and MQTT credentials. If you want to, you can also set the threshold for when the LED should turn on based on the soil moisture level, as well as how often the device should take measurements.

```
# Wi-Fi
WIFI_SSID = 'CHANGE_ME'  # Replace with your Wi-Fi network name
WIFI_PASS = 'CHANGE_ME'  # Replace with your Wi-Fi password

# MQTT CREDENTIALS
MQTT_SERVER = 'CHANGE_ME'  # Replace with your server address
MQTT_PORT = 1883           # Only replace if you've changed the default port
MQTT_USER = 'CHANGE_ME'    # Replace with your MQTT username
MQTT_KEY = 'CHANGE_ME'     # Replace with your MQTT password
MQTT_TOPIC = 'CHANGE_ME'   # Replace with the name of the MQTT topic
MQTT_CLIENT_ID = ubinascii.hexlify(unique_id())  # A unique string to use as the client ID

# APPLICATION LOGIC OPTIONS
MOISTURE_THRESHOLD = 30        # Change this to set what moisture level (%) the LED should turn on at (range: 0–100)
TIME_BETWEEN_MEASUREMENTS = 15 # How often (in seconds) the sensors should read data
```

---

### More detailed code explanation

The code for the different sensors and the LED is divided into separate classes to keep everything clean and modular.

__In total, there are three main classes I created:__

1. __MoistureSensor__: Includes methods to get readings from the soil moisture sensor.

2. __LDR__: Includes methods to get readings from the photoresistor sensor.

3. __LED__: Includes methods to control the LED, such as turning it on, off, or blinking.

---

__Libraries used:__

1. __DHT11__: This module is used to get readings from the DHT11 (temperature and humidity) sensor in a very simple way.

2. __MQTT__: This module from PyCom is used to connect to the MQTT broker and send messages.

3. __machine__: Provides functions related to hardware control on the Pico.

4. __network__: Used to connect the Pico to Wi-Fi.

5. __time__: Used to pause the program at different stages with the `sleep()` method.

6. __json__: Converts the measurements to JSON before sending them to the MQTT broker.

---

Since the code is separated into different classes, the main application loop (in `main.py`) is very simple. It reads all the sensors and returns the data as a dictionary. The moisture value is then checked, and if it is under the defined threshold, the LED turns on. Finally, the data is converted to JSON and sent to the MQTT broker.

__Main program loop:__

```
# Main Program Loop 
while True:
    try:
        data = readSensors()
        checkLEDStatus(data['moisture'])
        client.publish(topic=config.MQTT_TOPIC, msg=json.dumps(data))
        printToConsole(data)
    except Exception as error:
        led.blink(nrOfBlinks=3, speed=0.5)
        print("Exception occurred:", error)
    
    sleep(config.TIME_BETWEEN_MEASUREMENTS)  # Time between each measurement
```

---

__Read and return sensor data:__

```
# Read all sensors
def readSensors():
    # Get moisture level
    moisture = moistureSensor.readMoisture()
        
    # Get temperature and humidity
    thSensor.measure()
    temp = thSensor.temperature()
    humidity = thSensor.humidity()

    # Get light
    light = ldr.measure()

    # Save as dictionary 
    readings = {
        "moisture": moisture,
        "temp": temp,
        "humidity": humidity,
        "light": light
    }
      
    return readings
```

---

__Check moisture level:__

```
# Turn on LED if moisture level is under defined threshold
def checkLEDStatus(moisture):
    if moisture < config.MOISTURE_THRESHOLD:
        led.on()
    else:
        led.off()
```

---

__To provide user feedback, the LED blinks three times if an error occurs during the loop:__

```
def blink(self, nrOfBlinks, speed):
    count = 0

    while count < nrOfBlinks * 2:
        count += 1
        self.led.toggle()
        sleep(speed)
```

---

### MoistureSensor class

Since the `MoistureSensor` and `LDR` classes work very similarly, I’ll only explain the `MoistureSensor` class here:

```
class MoistureSensor:
    def __init__(self, dataPin, pwrPin):
        self.sensor = ADC(dataPin)
        self.pwrPin = Pin(pwrPin, Pin.OUT)
        self.MIN_MOISTURE = 63000  # Dry soil
        self.MAX_MOISTURE = 40000  # Just watered soil

    def turnOn(self):
        self.pwrPin.value(1)
        sleep(0.5)  # Pause to make sure the sensor is activated
  
    def turnOff(self):
        self.pwrPin.value(0)
     
    def readMoisture(self):
        self.turnOn()
        value = self.sensor.read_u16()
        moisture = self.__moistureInPercentage(value)
        self.turnOff()
        
        # print("RAW moisture level is {}".format(value))  # Use this to calibrate the sensor
        return moisture

    def __moistureInPercentage(self, value):
        moisture = round((self.MIN_MOISTURE - value) * 100 / (self.MIN_MOISTURE - self.MAX_MOISTURE))
        return max(0, min(moisture, 100))
```

This sensor is not designed to run continuously because that will corrode the sensor over time. Therefore, it is connected to a separate GPIO pin saved as a class property. This allows us to turn the sensor on only when taking a reading, then turn it off again. This helps prolong the sensor’s lifespan.

The sensor is also calibrated to get accurate measurements. This is done by measuring the raw ADC value when the sensor is in dry soil and in wet soil:

```
self.MIN_MOISTURE = 63000  # Dry soil
self.MAX_MOISTURE = 40000  # Just watered soil
```

_Note: These values can be changed if you want to recalibrate your sensor. Just uncomment `print("RAW moisture level is {}".format(value))` in the `readMoisture()` method, take new readings, and update the values accordingly._

---

When the `readMoisture()` method is called, it:

1. Turns on the sensor.
2. Reads the ADC value.
3. Converts it to a percentage using this formula:

   ```
   moisture = round((self.MIN_MOISTURE - value) * 100 / (self.MIN_MOISTURE - self.MAX_MOISTURE))
   return max(0, min(moisture, 100))
   ```

4. Turns off the sensor.
5. Returns the moisture value.

## Transmitting the data / connectivity

As mentioned, the Pico is connected to the internet via Wi-Fi. Since the device is meant to be located in a house, close to a router, there is no need to use another long-range protocol like LoRa. The Pico WH used in this tutorial has a built-in Wi-Fi chip, so this is also the most convenient solution.

To connect to Wi-Fi, the `connect()` function (in `/pico-code/lib/wifiConnect.py`) is called in the `boot.py` file, which runs when the device boots up. This function uses the __network__ module and the Wi-Fi credentials from `config.py` to establish a connection.

```
import config as keys
from time import sleep
import network

def connect():
    wlan = network.WLAN(network.STA_IF)  # Put modem in Station mode

    if not wlan.isconnected():  # Check if already connected
        print('Connecting to network...')
        wlan.active(True)  # Activate network interface

        # Set power mode to disable Wi-Fi power saving (if needed)
        wlan.config(pm=0xa11140)
        wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)  # Your Wi-Fi credentials
        print('Waiting for connection...', end='')

        # Wait for connection
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)

    # Print the IP assigned by the router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))

    return ip
```

_Note: If the connection fails, the red LED will flash 5 times._

---

### MQTT

To send the data to the database, the MQTT protocol is used. MQTT is a lightweight messaging protocol that is perfect for IoT devices because it is power-efficient and relatively simple to set up.

Using the MQTT library from PyCom, a connection is established to the MQTT broker, in my case Mosquitto, but it could also be Adafruit IO, for example. The connection uses the credentials stored in `config.py`.

```
# Client connection
client = MQTTClient(
    config.MQTT_CLIENT_ID,
    config.MQTT_SERVER,
    config.MQTT_PORT,
    config.MQTT_USER,
    config.MQTT_KEY
)
client.connect()
```

_Note: If you’re running Docker locally on your Mac (like I am), the `MQTT_SERVER` should be your Mac’s IP address. To get this, run `ipconfig getifaddr en0` in the terminal. If you don’t have a static IP address, this can change when you reconnect to your network. If it doesn’t connect, make sure this value is correct._

The sensor data is read, converted to JSON, and sent to the MQTT broker every 15 seconds by default. _This interval can be configured._

**Conversion to JSON and sending:**
```
client.publish(topic=config.MQTT_TOPIC, msg=json.dumps(data))
```

---

### Saving data to the database

Once the data is sent to the MQTT topic, __Telegraf__ collects the messages by subscribing to the same topic and saves them in the InfluxDB database. Because the data is sent as JSON and Telegraf is configured to handle JSON, the values are automatically parsed and placed into the correct fields in the InfluxDB bucket.

It is now possible to display this data in Grafana!

## Presenting the data

I used InfluxDB as the database since it is a time-series database designed to store timestamped data—perfect for visualizing measurements that change over time. It also integrates well with Grafana, since Grafana offers a built-in InfluxDB plugin that makes it easy to connect and query the database.

Telegraf is configured to check for new messages every 15 seconds, the same rate that the device publishes data. This interval can be adjusted in the `.env` file located in `/docker-tig-stack`.

Since I don’t need to store the data for long periods, InfluxDB is configured to automatically delete old data after 1 week. This can be changed in the bucket settings in the InfluxDB UI.

---

### Dashboard

In Grafana, I’ve built a dashboard to visualize the data stored in InfluxDB. It consists of live values displayed as gauges and time series graphs showing how the measurements change over time.

![Dashboard in Grafana](/assets/dashboard.png)

This is done using the Flux query language. All of the widgets are based on this query:

```
from(bucket: "plant-health")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_field"] == "moisture")
  |> yield(name: "result")
```

The query filters the data in InfluxDB by field. By changing `"moisture"` to the name of another field (for example, `"temp"` or `"humidity"`), you can set up additional widgets to display other measurements.

---

### Triggers

To notify me when I’m not home to see the LED, I set up a trigger in Grafana that sends a message to a Discord server using the webhook functionality. The message is sent when the latest soil moisture reading in the database is below 30%, the same threshold used to turn on the LED.

![Discord message](/assets/trigger.png)

If you’re interested in setting this up yourself, you can follow [this tutorial](https://grafana.com/docs/grafana/latest/alerting/configure-notifications/manage-contact-points/integrations/configure-discord/).

## Finalizing the design

That’s it!

You should now have a cool little device for your plant and a dashboard where you can see all the data it produces.

__Not a thirsty plant:__  
![Plant and device no led](/assets/demo_1.0.jpeg)
![Device no led](/assets/demo_2.1.jpeg)

__A thirsty plant:__  
![Plant and device](/assets/demo_2.0.jpeg)
![Device](/assets/demo_1.1.jpeg)

---

To improve this project further, it would be fun to 3D-print a case and solder the connections to make it more production-ready. Sadly, I don’t have a 3D printer or a soldering iron at the moment, so that isn’t possible right now.

The server is also running locally on my main MacBook, which is not ideal since it can’t stay online at all times. Investing in a Raspberry Pi or running the server on an old computer would be an improvement to the current solution. However, since everything runs in a Docker containers and managed with Docker-Compose, migrating it later should be fairly easy.

Another improvement would be to enable a way to dynamically change the moisture threshold. This could be done either via a front end where the Pico retrieves the value or with a physical dial on the device itself.

But for now, I think this is a very good start and I’m happy with it for my first IoT project.

---

_Note: Some things might have been skipped over in this tutorial or not explained in full detail — especially the configuration for the TIG stack. If I covered every step in depth, this tutorial would be way too long. There is some more instructions in `/docker-tig-stack/readme.md` and you can always Google if you run into any problems._ 🤯


