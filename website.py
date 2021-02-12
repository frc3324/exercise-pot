from flask import Flask, render_template
import sqlite3
import json

# Webserver shit
database = sqlite3.connect('exercises.db')
db = database.cursor()

app = Flask("Exercise Pot")

@app.route("/")
def website():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

# Exercise reminder and database shit
class Exercise:
    def __init__(self, name, days, duration, timeStart, repeats):
        # IS THIS HOW YOU DO IT
        self.name = name
        self.days = days
        self.duration = duration
        self.timeStart = timeStart
        self.repeats = repeats
        # Probably a horrible way to do this but idc just please god help me
        name = db.execute(f'SELECT name FROM exercises;')
        days = db.execute(f'SELECT days FROM exercises;')
        duration = db.execute(f'SELECT duration FROM exercises;')
        timeStart = db.execute(f'SELECT timeStart FROM exercises;')
        repeats = db.execute(f'SELECT repeats FROM exercises;')
    def serialize_data():
        json_out = {}
        json_out['Exercise Info'] = []
        json_out['Exercise Info'].append({
            # Come to think of it, this might just put each of the values as "Exercise.[value]. Oh well, won't know till we try it."
            'name' : Exercise.name,
            'days' : Exercise.days,
            'duration' : Exercise.duration,
            'timeStart' : Exercise.timeStart,
            'repeats' : Exercise.repeats
        })
        # If this doesn't work so help me god I will sudo rm -rf /*
        return json.dump(json_out)

db.execute('''
CREATE TABLE exercises(
name TEXT NOT NULL, 
days INT NOT NULL,
duration INT NOT NULL,
timeStart INT NOT NULL,
repeats INT NOT NULL);
''')
db.execute('''
INSERT INTO exercises(name, days, duration, timeStart, repeats)
VALUES ("cool exercise", 3, 60, 1200, 0);
''')
print(Exercise.serialize_data())
