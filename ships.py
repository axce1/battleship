import random
import pygame
from pygame.locals import *

class Korablic(object):
    ''' class work with ships '''

    def __init__(self):
        self.cells = set([])


    def addCell(self, cell):
        self.cells.add(cell)


    def draw(self, display, color):

        x = random.randrange(0,300,30)
        y = random.randrange(0,300,30)

        print x/30 , y/30
        x_kvadrat = x/30
        y_kvadrat = y/30
        self.addCell((x_kvadrat,y_kvadrat))
        print self.cells

        rect = Rect((y+32,x+32),(28,28))
        pygame.draw.rect(display,color,rect,0)

    def tadish(self, cell):
        self.cells.remove(cell)
        print self.cells




