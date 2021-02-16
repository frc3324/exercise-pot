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
VALUES ("cool exercise", 3, 60, 1200, 0);
''')

exerObj = Exercise("name", ["monday"], 120, 2200, 3)
print(serialize_data(exerObj))
