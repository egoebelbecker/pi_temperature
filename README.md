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

- [DS18B20 Digital Temperature Sensor](https://www.amazon.com/gp/product/B004G53D54/ref=as_li_ss_tl?imprToken=-b1psK3dKt4aW0Uqj7aUoA&slotNum=0&ie=UTF8&linkCode=ll1&tag=circbasi-20&linkId=c005e3037148903454c653b58f29a8d2)
- Raspberry Pi 3 B+ (or more powerful)
- Python 3.x, with the Flask package

The easiest way to install this is download or check it out from this repository.

### Reading the sensor

Wire the sensor as described [here.](https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/) 

Run the **tempsensor.py** script. It does not need to run with root privileges.

### Serving the web page

Run **server.py**. Point your web browser at the Raspberry Pi, on port 5000.





