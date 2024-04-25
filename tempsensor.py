#!/usr/bin/env python

import sys
import os
import glob
import time
import datetime
import json

#
# Configurable items:
# readings file name
# interval in seconds
# number of decimals
#

def read_config(config_file_name):
    try:
       with open(config_file_name, "r") as f:
          config = json.load(f)
          config["interval"] = int(config["interval"])
          config["decimals"] = int(config["decimals"])
          return config
    except Exception as e:
       print("Error reading config: {}".format(e))
       sys.exit() 

def get_devices(device_file):

    devices = []
    with open(device_file, "r") as f:
        device_list = json.load(f)
        devices = device_list["devices"]

    return devices

def get_device(entry):
    try:
       return glob.glob("/sys/bus/w1/devices/"+ entry)[0] + "/w1_slave"
    except Exception as e:
      print("Failed to get temp sensor device: {}".format(e))
      sys.exit()

def parse_reading(lines, decimals):
     try:
       equals_pos = lines[1].find("t=")
       if equals_pos != -1:
         temp_string = lines[1][equals_pos+2:]
         return(round(float(temp_string) / 1000.0, decimals))
     except Exception as e:
       print("Failed to p[arse reading: {}".format(e))
       sys.exit()

def check_lines(filename, max_items):
    with open(filename, 'r') as fin:
       data = fin.read().splitlines(True)
       readings_length = len(data)
       if readings_length > max_items:
         offset = readings_length - max_items
         with open(filename, 'w') as fout:
            fout.writelines(data[offset:])


def read_temp(decimals, interval, keep):

    while True:
        for entry in devices:
            device = get_device(entry["id"])
            print("Reading {}".format(device))
            try:
                timepoint = datetime.datetime.now()

                with open(device, "r") as sensor:
                    lines = sensor.readlines()
                while lines[0].strip()[-3:] != "YES":
                    time.sleep(0.2)
                    lines = read_temp_raw()

            except KeyboardInterrupt:
                break
            except Exception as e:
                print("Quitting on exception reading {}: {}".format(e, entry[id]))
                sys.exit()
 
            try:
                print(lines)
                timepassed = (datetime.datetime.now() - timepoint).total_seconds()
                temp = parse_reading(lines, decimals)
                readings_file = os.path.join(os.getcwd(), entry["name"] + ".txt")
                print(readings_file)
                with open(readings_file, "a+") as readings:
                    readings.write(time.strftime("%m-%d-%y %H:%M:%S,")+str(temp)+"\n")

                time.sleep(interval-timepassed)
                timepoint = datetime.datetime.now()
                check_lines(readings_file, keep)

            except KeyboardInterrupt:
                break
            except Exception as e:
                print("Quitting on exception processing result: {}".format(e))
                sys.exit()

if __name__ == "__main__":
    config = read_config("config.json")
    devices = get_devices(config["devices"])
    read_temp(config["decimals"], config["interval"], config["keep"])

