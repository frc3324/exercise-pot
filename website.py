from flask import Flask, render_template
import sqlite3

database = sqlite3.connect('exercises.db')
db = database.cursor()

app = Flask("Exercise Pot")

@app.route("/")
def website():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

class Exercise:
    name = db.execute(f'SELECT name FROM exercises;')
    days = db.execute(f'SELECT days FROM exercises;')
    duration = db.execute(f'SELECT duration FROM exercises;')
    timeStart = db.execute(f'SELECT timeStart FROM exercises;')
    repeats = db.execute(f'SELECT repeats FROM exercises;')
