#!/usr/bin/python
#coding: utf-8

from pygame.locals import *
import pygame
import random
import ships
import sys

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


def place_ship(cells):

    """
    вычисляем координаты корабля для передачи его объекту
    """
    while True:
        x = (random.randrange(0,300,30))/30
        y = (random.randrange(0,300,30))/30
        if ((x,y) not in allCells(KORABLIKY)) \
            and ((x,y) not in placeNearShip()):
            break
    return set([(x,y)])


def allCells(k):
    res = set ([])
    for kor in k:
        res = res.union(kor.cells)
    #print res
    return res


def placeNearShip():
    kol = set([])
    for x, y in allCells(KORABLIKY):
        for a in range(x-1,x+2):
            for b in range(y-1,y+2):
                if (a,b) != (x,y):
                    kol.add((a,b))
    return kol


def drawAllKorablics(koralblics):
    for kor in koralblics:
        kor.draw(DISPLAYSURF,OWNSHIPCOLOR)


def tadish(x,y):
    pygame.draw.line(DISPLAYSURF, (0, 0, 255), ((x*30)+59, 59+(y*30)), ((x*30)+32, (y*30)+32), 3)
    pygame.draw.line(DISPLAYSURF, (0, 0, 255), ((x*30)+64, (y*30)+32), ((x*30)+32, (y*30)+64), 3)
    print "удаляем кораблик"
    for i,j in enumerate(KORABLIKY):
        if (x,y) in j.cells:
            del KORABLIKY[i]


def vistrel(x, y):
    x = x/30 - 1
    y = y/30 - 1
    if (x,y) in allCells(KORABLIKY):
        tadish(x,y)
    else: print "you are miss!"


drawBoard(0)
drawBoard(350)

KORABLIKY=[]

for count in range(10):
    KORABLIKY.append(ships.Korablic(place_ship(allCells(KORABLIKY))))


drawAllKorablics(KORABLIKY)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            vistrel(mousex,mousey)
    pygame.display.update()

