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
readings_file = os.path.join(cwd, config["readings_file"])
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', refresh=config["interval"]*1000, location=config["location"])

@app.route('/readings')
def get_data():
    try:
       return send_file(readings_file, mimetype="text/csv", cache_timeout=0)
    except Exception as e:
       return str(e)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
