from flask import Flask, render_template, request

app = Flask(__name__)
number = "7"

@app.route('/')
def index():
    return render_template('index.html', number=number)

@app.route('/readings.txt')
def get_data():
    try:
	    return send_file('readings.txt', attachment_filename='readings.txt')
    except Exception as e:
		return str(e)

if __name__ == '__main__':
    app.run(debug=True)
