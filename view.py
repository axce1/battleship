#!/usr/bin/python
#coding: utf-8

from pygame.locals import *
import pygame
import sys

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

boardImage = pygame.image.load('sea.png')
DISPLAYSURF.blit(boardImage,(0,0))

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


def drawEnemyShip():
    pass


