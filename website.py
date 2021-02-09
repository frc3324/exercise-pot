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
        self.name = db.execute(f'SELECT name FROM exercises;')
        self.days = db.execute(f'SELECT days FROM exercises;')
        self.duration = db.execute(f'SELECT duration FROM exercises;')
        self.timeStart = db.execute(f'SELECT timeStart FROM exercises;')
        self.repeats = db.execute(f'SELECT repeats FROM exercises;')
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
