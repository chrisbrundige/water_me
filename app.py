# hello_world.py

from flask import Flask,render_template
app = Flask(__name__)
from moisture_sensor import getMoist


@app.route('/')
def hello_world():
    moist = getMoist()
    return render_template("index.html", moist = moist)



from app import app

if __name__ == '__main__':
    app.run(debug=True)