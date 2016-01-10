from __future__ import division

import random

class Item(object):

    # initiliaze
    def __init__(self, name, type, rarity):
        self.name = name
        self.type = type
        self.rarity = rarity

def pickRarity():
    rarityWeight1 = 150
    rarityWeight2 = 115
    rarityWeight3 = 55
    rarityWeight4 = 20
    rarityWeight5 = 5
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

def dropLoot():
    numItems = random.randint(0,3) + random.randint(0,2)
    for i in range(numItems):
        print pickRarity()

dropLoot()
