import random, sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# config
DATABASE = 'flaskr.db'
DEBUG = True

# rarity types
UNCOMMON = 1
COMMON = 2
REMARKABLE = 3
RARE = 4
MYTHICAL = 5

app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return "works"

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__ == '__main__':
    app.run(debug=True)
