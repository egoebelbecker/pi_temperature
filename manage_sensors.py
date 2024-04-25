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
       files = os.listdir(config["device_root"])
       for file in files:
           if file.startswith("28"):
               found_devices.append(file)

       
       for entry in found_devices:
           for device in devices:
               if entry == device["id"]:
                   print("Skipping {}".format(entry))
                   found_devices.remove(entry)               
                   break

       for entry in found_devices:
           print("New device: {}".format(entry))
           user_input = input("Enter a name: ")
           new_device = {"id": entry, "name": user_input}
           devices.append(new_device)


       with open(config["devices"], 'w') as outfile:
          json.dump(devices, outfile)

    except Exception as e:
      print("Failed to get temp sensor device: {}".format(e))
      sys.exit()





if __name__ == "__main__":
    config = read_config("config.json")
    devices = get_devices(config["devices"])
    print(print(json.dumps(devices, indent=4)))
