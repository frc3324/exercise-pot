import sqlite3
import json

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
VALUES ("cool exercise", "['monday']", 60, 1200, 0);
''')

exerObj = Exercise(
    db.execute("SELECT name FROM exercises;"), 
    db.execute("SELECT days FROM exercises;"), 
    db.execute("SELECT duration FROM exercises;"), 
    db.execute("SELECT timeStart FROM exercises"), 
    db.execute("SELECT repeats FROM exercises")
    )
print(serialize_data(exerObj))
