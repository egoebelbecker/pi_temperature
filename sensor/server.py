from flask import Flask, render_template
app = Flask(__name__)
number = "7"

@app.route('/')
def index():
    return render_template('index.html', number=number)

if __name__ == '__main__':
    app.run(debug=True)
