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
    def __init__():
        Exercise.name = db.execute(f'SELECT name FROM exercises;')
        Exercise.days = db.execute(f'SELECT days FROM exercises;')
        Exercise.duration = db.execute(f'SELECT duration FROM exercises;')
        Exercise.timeStart = db.execute(f'SELECT timeStart FROM exercises;')
        Exercise.repeats = db.execute(f'SELECT repeats FROM exercises;')
    def serialize_data():
        json_out = {}
        json_out['Exercise Info'] = []
        json_out['Exercise Info'].append({
            'name' : Exercise.name,
            'days' : Exercise.days,
            'duration' : Exercise.duration,
            'timeStart' : Exercise.timeStart,
            'repeats' : Exercise.repeats
        })
        return json.dump(json_out)