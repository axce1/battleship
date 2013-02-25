# -*- coding: utf-8 -*-
import random

class Korablic(object):
    ''' class work with ships
    '''

    def  __init__(self):
        self.cells = set ([])
        self.hitspace = set([])

    def addCell(self, cell):
        if isinstance(cell, set):
            self.cells = self.cells.union(cell)
        else:
            self.cells.add(cell)

    def tadish(self, cell):
        self.cells.remove(cell)
        if len(self.cells) != 0:
            self.hitspace.add(cell)
        else:
            self.isDead()

    def isDead(self):
        print 'korablik mertvii'


class workShip(object):

    def __init__(self):
        self.korabli=[]

    def createListShips(self):

        for c in range(1):
            ship = Korablic()
            ship.addCell(self.genDeckShip(4))
            self.korabli.append(ship)

        for c in range(3):
            ship = Korablic()
            ship.addCell(self.genDeckShip(2))
            self.korabli.append(ship)

        for c in range(2):
            ship = Korablic()
            ship.addCell(self.genDeckShip(3))
            self.korabli.append(ship)

        for c in range(4):
            ship = Korablic()
            ship.addCell(self.genShipPlace())
            self.korabli.append(ship)

        return self.korabli

    def shipCells(self):

        spa = set([])
        for ekor in self.korabli:
            spa = spa.union(ekor.cells)
        return spa

    def placeNearShip(self):

        kol = set([])
        for x,y in self.shipCells():
            for a in range(x-1,x+2):
                for b in range(y-1,y+2):
                    if (a,b) != (x,y):
                        kol.add((a,b))
        return kol

    def genShipPlace(self):

        allspace = set([])

        for i in range(0,10):
            for j in range(0,10):
                allspace.add((i,j))

            space = allspace - (self.shipCells().union(self.placeNearShip()))
            ship = random.sample(space, 1)


        return ship[0]

    def genDeckShip(self, deck):

        allspace = set([])
        for i in range(0,10):
            for j in  range(0,10):
                allspace.add((i,j))
                space = allspace - (self.shipCells().union(self.placeNearShip()))

        shiplist = []
        for x, y in space:
            z = self.generaciyaZ(x,y,deck)
            for i in z:
                if i.issubset(space):
                    shiplist.append(i)

        deck2ship = random.sample(shiplist,1)[0]
        return deck2ship


    def generaciyaZ(self, x, y, deck):
        if deck == 2:
            z = set([])
            w = set([])
            z.add((x,y))
            z.add((x,y+1))
            w.add((x,y))
            w.add((x+1,y))
            return [z,w]

        elif deck == 3:
            z = set([])
            w = set([])
            z.add((x,y))
            z.add((x,y+1))
            z.add((x,y+2))
            w.add((x,y))
            w.add((x+1,y))
            w.add((x+2,y))
            return [z,w]

        elif deck == 4:
            z = set([])
            w = set([])
            z.add((x,y))
            z.add((x,y+1))
            z.add((x,y+2))
            z.add((x,y+3))
            w.add((x,y))
            w.add((x+1,y))
            w.add((x+2,y))
            w.add((x+3,y))
            return [z,w]

