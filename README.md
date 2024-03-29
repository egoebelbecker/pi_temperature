# pi_temperature


A very basic set of scripts for reading a temperature via Raspberry Pi and charting it in a web browser.

![](trimmed.gif)

## Files

**tempsensor.py** - reads the temperature, saves to a text file with a timestamp

**config.json** - configuration for tempsensor.py

**server.py** - serves chart and temperature readings to browser

**templates/fetch.html** - web app


## Installation and Usage


### Requirements

- [DS18B20 Digital Temperature Sensor](https://amzn.to/3vyjapy) and associated wiring, circuitry, etc.
- Raspberry Pi 3 B+ - this is what I used. It may work on smaller models with less memory.
- Python 3.x, with the Flask package.

The easiest way to install this is download or check it out from this repository.

### Reading the sensor

Wire the sensor as described [here.](https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/) 

Configure the script:

``{
   "interval": "30",
   "readings_file": "readings.txt",
   "decimals": "2"
}

**interval** - how frequently to poll the temperarture, in seconds.
**readings_file** - where the readiongs are stored. If you change this, you'll need to update the webserver and web page.
**decimals** - number of figure to keep after the decimal in the temperature.


Run the **tempsensor.py** script. It does not need to run with root privileges. It expects to find **config.json** in the current working directory, and will store the readings in its current directory.



### Serving the web page

Run **server.py**. Point your web browser at the Raspberry Pi, on port 5000.





