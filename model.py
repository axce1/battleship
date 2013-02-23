
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
          #  ship.addCell(self.generPlaceShip())
            ship.addCell(self.genShipPlace())
            self.korabli.append(ship)

        return self.korabli

    def generPlaceShip(self, deck, k=0):

        if deck == 1:
            while True:
                x = (random.randrange(0,300,30))/30
                y = (random.randrange(0+k,300+k,30))/30

                if ((x,y) not in self.shipCells()) \
                    and ((x,y) not in self.placeNearShip()):
                    break
            return set([(x,y)])

        if deck == 2:
            while True:
                x = (random.randrange(0,300,30))/30
                y = (random.randrange(0+k,300+k,30))/30

                if ((x,y) not in self.shipCells()) \
                    and ((x,y) not in self.placeNearShip()):
                    break

            while True:
                while True:
                    if random.randint(0,1) == 0:
                        q = x - random.randint(-1,1)
                        w = y

                        if (0 < q or q > 9) and q != x:
                            break
                    else:
                        q = x
                        w = y - random.randint(-1,1)

                        if  w != y and ((0 < w or w > 9) \
                             or (12 < w or w > 21)):
                            break

                if ((q,w) not in self.shipCells()) \
                   and ((q,w) not in self.placeNearShip()):
                    break

        return set([(x,y),(q,w)])

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

    def genShipPlace(self):

        allspace = set([])
        for i in range(0,10):
            for j in range(0,10):
                allspace.add((i,j))

        space = allspace - (self.shipCells().union(self.placeNearShip()))
        ship = random.sample(space, 1)
        return ship[0]
