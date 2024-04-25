import os
import sys
import json
from flask import Flask, render_template, send_file


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


config = read_config("config.json")
cwd = os.getcwd()
devices_file = os.path.join(cwd, config["devices"])
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', refresh=config["interval"]*1000, location=config["location"])

@app.route('/<readings>')
def get_data(readings):
   try:
      readings_file = os.path.join(cwd, readings + ".txt")
      if readings == "chart.js":
         return send_file("chart.js", mimetype="application/javascript", max_age=0) 
      else:
       return send_file(readings_file, mimetype="text/csv", max_age=0)
   except Exception as e:
       return str(e)

@app.route('/devices')
def get_devices():
    try:
       return send_file(devices_file, mimetype="application/json", max_age=0)
    except Exception as e:
       return str(e)



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
