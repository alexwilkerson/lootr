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
    cur = g.db.execute("SELECT id, name FROM items WHERE rarity=? ORDER BY RANDOM() LIMIT 1", [rarity])
    row = cur.fetchone()

    item = dict(idNum=row[0], name=row[1])

    return item

def sim(n):
    total = n
    totalnum = 0
    rar1 = 0
    rar2 = 0
    rar3 = 0
    rar4 = 0
    rar5 = 0
    rar6 = 0
    rar7 = 0
    while n > 0:
        rar = pickRarity()
        if rar == 1:
            rar1 += 1
        if rar == 2:
            rar2 += 1
        if rar == 3:
            rar3 += 1
        if rar == 4:
            rar4 += 1
        if rar == 5:
            rar5 += 1
        if rar == 6:
            rar6 += 1
        if rar == 7:
            rar7 += 1
        n -= 1
        totalnum += 1
    print "1 = {}/{}%\n2 = {}/{}%\n3 = {}/{}%\n4 = {}/{}%\n5 = {}/{}%\n6 = {}/{}%\n7 = {}/{}%".format(rar1, rar1/total*100,
                                                                                                 rar2, rar2/total*100,
                                                                                                 rar3, rar3/total*100,
                                                                                                 rar4, rar4/total*100,
                                                                                                 rar5, rar5/total*100,
                                                                                                 rar6, rar6/total*100,
                                                                                                 rar7, rar7/total*100)
    print totalnum

@app.route('/')
def dropLoot():
    numItems = random.randint(0,2) + random.randint(0,2) + random.randint(0,1)
    if numItems == 0:
        return "You open the chest to find...nothing."
    else:
        loot = ""
        for i in range(numItems):
            newItem = getItem(pickRarity())
            loot += "<a href=/item/" + str(newItem['idNum']) +  ">" + newItem['name'] + "</a><br />"
        return loot

@app.route('/item/<int:id>')
def itemPage(id):
    cur = g.db.execute('select name, description, type, quality, rarity, is_unique from items where id = ?', [str(id)])
    row = cur.fetchone()
    if row == None:
        return "QQ u sneaky little bastard. there is nothing here for U.  !!!---"
    item = dict(name=row[0], description=row[1], type=row[2], quality=row[3], rarity=row[4], is_unique=row[5])
    return render_template('item.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)
