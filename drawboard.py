#!/usr/bin/python
#coding: utf-8

from pygame.locals import *
import pygame
import ships
import random

GRIDLINECOLOR = (0,0,0)
OWNSHIPCOLOR = (138,0,184)

WINDOWWIDTH = 710
WINDOWHEIGHT = 350
SPACESIZE = 30
BOARDWIDTH = 10
BOARDHEIGHT =10

XMARGIN = 30
YMARGIN = 30

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

boardImage = pygame.image.load('sea.png')
DISPLAYSURF.blit(boardImage,(0,0))

def drawBoard(pix):

    for x in range(BOARDWIDTH + 1):

        startx = (x * SPACESIZE) + XMARGIN
        starty = YMARGIN
        endx = (x * SPACESIZE) + XMARGIN
        endy = YMARGIN + (BOARDHEIGHT * SPACESIZE)
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR,(startx+pix,starty),(endx+pix,endy),2)

    for y in range(BOARDHEIGHT + 1):

        startx = XMARGIN
        starty = (y * SPACESIZE) + YMARGIN
        endx = XMARGIN + (BOARDWIDTH * SPACESIZE)
        endy = (y * SPACESIZE) + YMARGIN
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx+pix, starty),(endx+pix,endy),2)


def drawNotOwnBoaard(pix):

    for x in range(BOARDWIDTH + 1):

        startx = (x * SPACESIZE) + (XMARGIN+350)
        starty = YMARGIN
        endx = (x * SPACESIZE) + (XMARGIN+350)
        endy = YMARGIN + (BOARDHEIGHT * SPACESIZE)
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR,(startx,starty),(endx,endy))

    for y in range(BOARDHEIGHT + 1):

        startx = XMARGIN+350
        starty = (y * SPACESIZE) + (YMARGIN+0)
        endx = (XMARGIN+350) + (BOARDWIDTH * SPACESIZE)
        endy = (y * SPACESIZE) + (YMARGIN+0)
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx, starty),(endx,endy))



drawBoard(0)
drawBoard(350)

def place_ship():

    """
    вычисляем координаты корабля для передачи его объекту
    """

    x = random.randrange(0,300,30)
    y = random.randrange(0,300,30)
    #if ((x,y) not in allCells(KORABLIKY)):
        #((x/30, y/30) not in self.nonempty):
    #    print 'hoho'
    return set([(x,y)])



def allCells(k):
    res = set ([])
    for kor in k:
        res = res.union(kor.cells)
    print res
    return res


ship1 = ships.Korablic(place_ship())
ship2 = ships.Korablic(place_ship())
ship3 = ships.Korablic(place_ship())

KORABLIKY=[ship1,ship2,ship3]

allCells(KORABLIKY)


def drawAllKorablics(koralblics):
    for kor in koralblics:
        kor.draw(DISPLAYSURF,OWNSHIPCOLOR)


drawAllKorablics(KORABLIKY)

while True:

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            print mousex, mousey
            a.vistrel(mousex,mousey)
    pygame.display.update()

