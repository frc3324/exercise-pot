from flask import Flask, render_template
import sqlite3
import json

# Database and JSON serialization shit

database = sqlite3.connect('exercises.db')
db = database.cursor()

class Exercise(object):
    def __init__(self, name, days, duration, timeStart, repeats):
        # IS THIS HOW YOU DO IT
        self.name = name
        self.days = days
        self.duration = duration
        self.timeStart = timeStart
        self.repeats = repeats

def serialize_data(exer):
    return json.dumps(exer.__dict__)

db.execute('''
INSERT INTO exercises(name, days, duration, timeStart, repeats)
VALUES ("cool exercise", 3, 60, 1200, 0);
''')

exerObj = Exercise("name", ["monday"], 120, 2200, 3)
print(serialize_data(exerObj))

db.execute('''
INSERT INTO exercises(name, days, duration, timeStart, repeats)
VALUES ("cool exercise", 3, 60, 1200, 0);
''')
print(serialize_data(exerObj))

# Webserver shit
app = Flask("Exercise Pot")

@app.route("/")
def website():
    return "Hello World!"

if __name__ == "__main__":
    app.run()