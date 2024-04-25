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

def check_devices(devices):
    try:
       found_devices = []
       files = os.listdir("/sys/bus/w1/devices/")
       for file in files:
           if file.startswith("28"):
               print("Found {}".format(file))
               found_devices.append(file)


       for entry in found_devices:
           print("Looking for {}".format(entry))
           found = False
           for device in devices:
               if entry == device["id"]:
                   print("Skipping {}".format(entry))
                   found = True

           if not found:
              print("\nNew device: {}".format(entry))
              user_input = input("Enter a name: ")
              new_device = {"id": entry, "name": user_input}
              devices.append(new_device)


       with open(config["devices"], 'w') as outfile:
          device_list = {}
          device_list["devices"] = devices
          json.dump(device_list, outfile)

    except Exception as e:
      print("Failed to get temp sensor device: {}".format(e))
      sys.exit()

