#!/usr/bin/env python

import sys
import os
import glob
import time
import datetime
import json
import csv



def read_config(config_file_name):
    try:
       with open(config_file_name, "r") as f:
          config = json.load(f)
          config["interval"] = int(config["interval"])
          config["decimals"] = int(config["decimals"])
          config["keep"] = 86400/config["interval"]
          return config
    except Exception as e:
       print("Error reading config: {}".format(e))
       sys.exit() 




def get_devices(config):

    devices = []
    with open(config["devices"], newline='') as f:
        csvfile = csv.reader(f)    
        for row in csvfile:
            devices.append(row)

    return devices


if __name__ == "__main__":
    config = read_config("config.json")
    devices = get_devices(config)
    for row in devices:
        print(row[0], row[1])
