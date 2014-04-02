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
        self.hitspace.add(cell)
        a = self.hitspace
        self.cells.remove(cell)
        z = self.cells

    def isDead(self):
        if len(self.cells) == 0:
            print 'korablik mertvii'


class workShip(object):

    def __init__(self):
        self.korabli=[]
        self.bumspace = set([])

    def createListShips(self):

        for c in range(4):
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

        for c in range(1):
            ship = Korablic()
            ship.addCell(self.genShipPlace())
            self.korabli.append(ship)


    def delFromKorabli(self, x, y):
        for i in self.korabli:
            if (x,y) in i.cells:
                i.tadish((x,y))
                return 'tada'

    def bumSpace(self,x,y):
        self.bumspace.add((x,y))

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
            try:
                ship = random.sample(space, 1)
            except:
                print ('корабли', ship)
                print ('пространство', space)
                print 'корабль уже есть в этом месте'


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
            for i in range(2):
                z.add((x,y+i))
                w.add((x+i,y))
            return [z,w]

        elif deck == 3:
            z = set([])
            w = set([])
            for i in range(3):
                z.add((x,y+i))
                w.add((x+i,y))
            return [z,w]

        elif deck == 4:
            z = set([])
            w = set([])
            for i in range(4):
                z.add((x,y+i))
                w.add((x+i,y))
            return [z,w]

