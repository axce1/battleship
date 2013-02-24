
import random

class Korablic(object):
    ''' class work with ships
    '''

    def  __init__(self):
        self.cells = set ([])
        self.nonempty = set([])

    def addCell(self, cell):
        self.cells.add(cell)

    def tadish(self, cell):
        pass

    def isDead(self,cell):
        pass


class workShip(object):

    def __init__(self):
        self.korabli=[]

    def createListShips(self, k):

        if k == 'own':
            for c in range(5):
                ship = Korablic()
                ship.addCell(self.genShipPlace(k))
                self.korabli.append(ship)

        #    for c in range(3):
                #ship = Korablic()
                #ship.addCell(self.gen2deckship())
                #self.korabli.append(ship)

        elif k == 'enemy':
             for c in range(5):
                ship = Korablic()
                ship.addCell(self.genShipPlace(k))
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
          #  for x,y in j:
            for a in range(x-1,x+2):
                for b in range(y-1,y+2):
                    if (a,b) != (x,y):
                        kol.add((a,b))
        return kol

    def genShipPlace(self, k):

        allspace = set([])

        if k == 'own':
            for i in range(0,10):
                for j in range(0,10):
                    allspace.add((i,j))

            space = allspace - (self.shipCells().union(self.placeNearShip()))
            ship = random.sample(space, 1)

        elif k == 'enemy':
            for i in range(0,10):
                for j in range(12,22):
                    allspace.add((i,j))

            space = allspace - (self.shipCells().union(self.placeNearShip()))
            ship = random.sample(space, 1)

        return ship[0]

    def gen2deckship(self):

        allspace = set([])
        for i in range(0,10):
            for j in  range(0,10):
                allspace.add((i,j))
        space = allspace - (self.shipCells().union(self.placeNearShip()))

        shiplist = []
        for x, y in space:
            z = set([])
            z.add((x,y))
            z.add((x,y+1))
            shiplist.append(z)

        deck2ship = random.sample(shiplist,1)[0]
        print deck2ship
        return deck2ship



