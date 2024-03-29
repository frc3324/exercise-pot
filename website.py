from flask import Flask, render_template, send_from_directory
from flask_cors import CORS

import sqlite3
import json

# Database and JSON serialization shit

class Exercise(object):
    def __init__(self, name, days, duration, timeStart, repeats):
        # IS THIS HOW YOU DO IT
        self.name = name 
        self.days = days
        self.duration = duration
        self.timeStart = timeStart
        self.repeats = repeats

    def serialize_data(self):
        return json.dumps(self.__dict__)

# Webserver shit
app = Flask("Exercise Pot")
CORS(app)

@app.route("/easy.json")
def easy():
    return open('easy.json', 'r').read()

@app.route("/med.json")
def med():
    return open('med.json', 'r').read()

@app.route("/workout.html")
def workout():
    return open('frontend/workout.html', 'r').read()

@app.route("/")
def index():
    return open('frontend/workout-calendar.html', 'r').read()


@app.route('/<path:path>')
def dir(path):
    return send_from_directory('.', path)

@app.route('/frontend/<path:path>')
def frontend(path):
    return send_from_directory('frontend', path)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
