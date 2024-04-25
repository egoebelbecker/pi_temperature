#!/usr/bin/env python

import sys
import os
import glob
import json

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

def get_devices(device_file):

    devices = []
    with open(device_file, "r") as f:
        device_list = json.load(f)
        devices = device_list["devices"]

    return devices






if __name__ == "__main__":
    config = read_config("config.json")
    devices = get_devices(config["devices"])
    print(devices)    