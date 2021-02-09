from flask import Flask, render_template
import sqlite3
import json

database = sqlite3.connect('exercises.db')
db = database.cursor()

app = Flask("Exercise Pot")

@app.route("/")
def website():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

class Exercise:
    def __init__(self, name, days, duration, timeStart, repeats):
        self.name = name
        self.days = days
        self.duration = duration
        self.timeStart = timeStart
        self.repeats = repeats
        name = db.execute(f'SELECT name FROM exercises;')
        days = db.execute(f'SELECT days FROM exercises;')
        duration = db.execute(f'SELECT duration FROM exercises;')
        timeStart = db.execute(f'SELECT timeStart FROM exercises;')
        repeats = db.execute(f'SELECT repeats FROM exercises;')
    def serialize_data():
        json_out = {}
        json_out['Exercise Info'] = []
        json_out['Exercise Info'].append({
            'name' : self.name,
            'days' : self.days,
            'duration' : self.duration,
            'timeStart' : self.timeStart,
            'repeats' : self.repeats
        })
        return json.dump(json_out)
