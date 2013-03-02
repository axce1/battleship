#!/usr/bin/python
#coding: utf-8

from pygame.locals import *
import pygame

GRIDLINECOLOR = (0,0,0)
OWNSHIPCOLOR = (61,139,255)
ENEMYSHIPCOLOR = (138,0,184)

#color = OWNSHIPCOLOR

WINDOWWIDTH = 720
WINDOWHEIGHT = 360
SPACESIZE = 30
BOARDWIDTH = 10
BOARDHEIGHT =10

XMARGIN = 30
YMARGIN = 30

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

boardImage = pygame.image.load('data/sea.png')
DISPLAYSURF.blit(boardImage,(0,0))

shipImage = pygame.image.load('data/ship.png')
shipImage = pygame.transform.scale(shipImage, (30,32))

def drawBoard(pix=0):

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


def drawShip(display, color, ship, pix):

    if len(ship.cells) == 1:
        x,y = list(ship.cells)[0]
        ship_place = ((y*30+pix)+30,(x*30)+30)
        DISPLAYSURF.blit(shipImage,ship_place)
    else:
        for x,y in ship.cells:
            rect = Rect(((y*30+pix)+32,(x*30)+32),(28,28))
            pygame.draw.rect(display,color,rect,0)


def drawAllShip(korablics, color, q) :
    if q == 'own':
        pizda = 0
    else:
        pizda = 360
    for k in korablics:
        drawShip(DISPLAYSURF, color, k, pizda)


def drawEnemyShip(display, ships, x, y ,pix=360):
    for k in ships.korabli:
        if (x,y) in k.hitspace:
            rect = Rect(((x*30+pix)+32,(y*30)+32),(28,28))
            pygame.draw.rect(display, ENEMYSHIPCOLOR,rect,0)


def reDrawAll(korablics, ship, color, q, display, x, y, pix=360):
    drawBoard()
    drawBoard(360)
    drawAllShip(korablics, color, q)
    drawEnemyShip(display,ship, x, y, pix=360)

