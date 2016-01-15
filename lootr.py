from __future__ import division

import random, sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# configuration
DATABASE = 'lootr.db'
DEBUG = True

# rarity types
UNCOMMON = 1
COMMON = 2
REMARKABLE = 3
RARE = 4
MYTHICAL = 5

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def pickRarity():
    rarityWeight1 = 250
    rarityWeight2 = 25
    rarityWeight3 = 15
    rarityWeight4 = 6
    rarityWeight5 = 2
    rarityWeight6 = 0.5
    rarityWeight7 = 0.05
    totalWeight = rarityWeight1 + rarityWeight2 + rarityWeight3 + rarityWeight4 + rarityWeight5 + rarityWeight6 + rarityWeight7
    r = random.random() * totalWeight

    if r < rarityWeight7:
        return 7
    elif r < rarityWeight6 + rarityWeight7:
        return 6
    elif r < rarityWeight5 + rarityWeight6 + rarityWeight7:
        return 5
    elif r < rarityWeight4 + rarityWeight5 + rarityWeight6 + rarityWeight7:
        return 4
    elif r < rarityWeight3 + rarityWeight4 + rarityWeight5 + rarityWeight6 + rarityWeight7:
        return 3
    elif r < rarityWeight2 + rarityWeight3 + rarityWeight4 + rarityWeight5 + rarityWeight6 + rarityWeight7:
        return 2
    else:
        return 1

def getItem(rarity):
    cur = g.db.execute("SELECT id, name, quality FROM items WHERE rarity=? ORDER BY RANDOM() LIMIT 1", [rarity])
    row = cur.fetchone()

    item = dict(idNum=row[0], name=row[1], quality=row[2])

    return item

@app.route('/')
def dropLoot():
    numItems = random.randint(0,2) + random.randint(0,2) + random.randint(0,1)
    if numItems == 0:
        loot = "...nothing."
        return render_template("index.html", loot=loot)
    else:
        loot = str(random.randint(0,30)) + " gold pieces.<br />"
        for i in range(numItems):
            newRarity = pickRarity()
            newItem = getItem(newRarity)
            newQuality = newItem["quality"]
            qualityColor = {1:"saddlebrown",2:"lightseagreen",3:"steelblue",4:"rebeccapurple",5:"darkorange"}
            loot += "<a href=/item/" + str(newItem['idNum']) +  " style='color: " + qualityColor[newQuality] + "'>" + newItem['name'] + "</a><br />"
        return render_template("index.html", loot=loot)

@app.route('/item/<int:id>')
def itemPage(id):
    cur = g.db.execute('select name, description, type, quality, rarity, is_unique from items where id = ?', [str(id)])
    row = cur.fetchone()
    if row == None:
        return "QQ u sneaky little bastard. there is nothing here for U.  !!!---"
    item = dict(name=row[0], description=row[1], type=row[2], quality=row[3], rarity=row[4], is_unique=row[5])
    return render_template('item.html', item=item)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
