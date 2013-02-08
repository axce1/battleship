import random
import pygame
from pygame.locals import *

class Korablic(object):
    ''' class work with ships '''

    def __init__(self,sh_set):
        self.cells = sh_set
        self.nonempty = set([])


    def addCell(self, cell):
        '''add ships to set cells'''
        self.cells.add(cell)

    def draw(self, display, color):

      #  '''draw ship method'''

        #while True:
            #x = random.randrange(0,300,30)
            #y = random.randrange(0,300,30)
            #if ((x/30,y/30) not in self.cells) and \
                #((x/30, y/30) not in self.nonempty):
                #break

        #x_k = x/30
        #y_k = y/30

        #self.addCell((x_k,y_k))
        self.addNonEmpty()
        print self.cells
        print self.nonempty

        for y, x in self.cells:

            rect = Rect((y+32,x+32),(28,28))
            pygame.draw.rect(display,color,rect,0)

    def  tadish(self, cell):
        self.cells.remove(cell)
        print self.cells
        print 'delete'

    def vistrel(self, x, y):

        if ((y/30)-1,(x/30)-1) in self.cells:
            print 'ta-da'
            print y, x
            self.tadish((((y/30)-1,(x/30)-1)))
        else:
            print 'loser!!!'


    def addNonEmpty(self):
        """ add non empty space to set nonempty"""

        for x,y in self.cells:
            pass

        print x/30,y/30

        for a in range(x-1,x+2):
            for b in range(y-1,y+2):
                if (a,b) != (x,y) \
                    and (10 > a > -1) and (10 > b > -1):
                        self.nonempty.add((a,b))




