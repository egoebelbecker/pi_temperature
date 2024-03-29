from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('fetch.html')

@app.route('/readings.txt')
def get_data():
    try:
       return send_file('/home/pi/pi_temperature/readings.txt', mimetype="text/csv", cache_timeout=0)
    except Exception as e:
       return str(e)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
