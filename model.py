
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

    def createListShips(self):
        for c in range(5):
            ship = Korablic()
            ship.addCell(self.generPlaceShip())
            self.korabli.append(ship)

        return self.korabli

    def generPlaceShip(self, k=0):

        while True:
            x = (random.randrange(0,300,30))/30
            y = (random.randrange(0+k,300+k,30))/30
            #print self.x
            #print self.y

            if ((x,y) not in self.shipCells()) \
                and ((x,y) not in self.placeNearShip()):
                break
        return ((x,y))

    def shipCells(self):

        self.spa = set([])
        for ekor in self.korabli:
            self.spa = self.spa.union(ekor.cells)
        return self.spa

    def hoho(self):
        self.hui = set([])
        for x in self.korabli:
            self.hui = self.hui.union(x.cells)
        print self.hui

    def placeNearShip(self):

        self.kol = set([])
        for x,y in self.shipCells():
            for a in range(x-1,x+2):
                for b in range(y-1,y+2):
                    if (a,b) != (x,y):
                        self.kol.add((a,b))
        return self.kol


