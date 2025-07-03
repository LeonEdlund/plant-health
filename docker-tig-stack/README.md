## Set Up

These instructions explain how to get the TIG stack and Mosquitto running on a Mac.  
They should be very similar on other operating systems.

_Note: This will run locally on your computer and will __not__ be accessible from other networks._

0. Clone this repo.

1. Install [Docker Desktop](https://docs.docker.com/desktop/setup/install/mac-install/).

2. Install Mosquitto using Homebrew:  
   `brew install mosquitto`

3. Open a terminal and navigate to the `docker-tig-stack` folder:  
   `cd /path/to/docker-tig-stack`

4. Create a Mosquitto password file (you can pick any username):  
   `mosquitto_passwd -c ./mosquitto/config/passwd YOUR_USERNAME`

5. Provide a password when prompted.

6. Edit the `.env` file and set:  
   - Your newly created Mosquitto username and password.  
   - A name for the MQTT topic you want to use. _(This must match the topic configured in your Pico `config.py`.)_

7. In the `.env` file, also set a username and password for Grafana.  
   _(These credentials will be used to log in to Grafana at [http://127.0.0.1:3000](http://127.0.0.1:3000))._

8. Start the Docker container:  
   `docker-compose up`

9. Open [http://127.0.0.1:8086](http://127.0.0.1:8086) in your browser and complete the InfluxDB setup wizard.  
   _Make sure to save the credentials and the generated API token, you will need them in the next step._

10. When the InfluxDB setup is finished, stop the Docker container:  
    `docker-compose down`

11. Edit your `.env` file again and add:  
    - The InfluxDB username  
    - The InfluxDB password  
    - The organization name  
    - The bucket name  
    - The API token

12. Start the Docker containers again:  
    `docker-compose up`

13. Once everything is running, open [http://127.0.0.1:3000](http://127.0.0.1:3000) to access Grafana.  
    Log in with your Grafana credentials and add InfluxDB as a data source.  
    You can now create dashboards to visualize your data.

More info on working with InfluxDB and Grafana can be found [here](https://grafana.com/docs/grafana/latest/getting-started/get-started-grafana-influxdb/) 