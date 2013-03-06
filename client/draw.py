#!/usr/bin/python
#coding: utf-8

from pygame.locals import *
import pygame
import control

GRIDLINECOLOR = (0,0,0)
OWNSHIPCOLOR = (61,139,255)
ENEMYSHIPCOLOR = (138,0,184)

WINDOWWIDTH = 720
WINDOWHEIGHT = 360
SPACESIZE = 30
BOARDWIDTH = 10
BOARDHEIGHT =10

XMARGIN = 30
YMARGIN = 30

pygame.init()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf',50)
    titleSurf1 = titleFont.render('Start Cool Game?',True, ENEMYSHIPCOLOR)
    titleRect = titleSurf1.get_rect()
    titleRect.center = (WINDOWWIDTH/2, WINDOWHEIGHT/2)
    DISPLAYSURF.blit(titleSurf1,titleRect)
    while True:
        if control.checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()


def drawBoard():

    boardImage = pygame.image.load('data/sea.png')
    DISPLAYSURF.blit(boardImage,(0,0))

    for x in range(BOARDWIDTH + 1):
        ## draw left
        startx = (x * SPACESIZE) + XMARGIN
        starty = YMARGIN
        endx = (x * SPACESIZE) + XMARGIN
        endy = YMARGIN + (BOARDHEIGHT * SPACESIZE)
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR,(startx,starty),(endx,endy),2)
        ## draw left
        startx = (x * SPACESIZE) + XMARGIN
        starty = YMARGIN
        endx = (x * SPACESIZE) + XMARGIN
        endy = YMARGIN + (BOARDHEIGHT * SPACESIZE)
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR,(startx+360,starty),(endx+360,endy),2)


    for y in range(BOARDHEIGHT + 1):
        ## draw left
        startx = XMARGIN
        starty = (y * SPACESIZE) + YMARGIN
        endx = XMARGIN + (BOARDWIDTH * SPACESIZE)
        endy = (y * SPACESIZE) + YMARGIN
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx, starty),(endx,endy),2)
        ## draw right
        startx = XMARGIN
        starty = (y * SPACESIZE) + YMARGIN
        endx = XMARGIN + (BOARDWIDTH * SPACESIZE)
        endy = (y * SPACESIZE) + YMARGIN
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx+360, starty),(endx+360,endy),2)


def drawShip(display, ship, pix=0):

    shipImage = pygame.image.load('data/ship.png')

    cell = ship.hitspace.union(ship.cells)

    if len(cell) == 1:
        x,y = list(cell)[0]
        ship_place = ((y*30+pix)+30,(x*30)+30)
        shipImage = pygame.transform.scale(shipImage, (30,30))
        DISPLAYSURF.blit(shipImage,ship_place)
    elif len(cell) == 2:
        x,y = min(list(cell))
        ship_place = ((y*30+pix)+30,(x*30)+30)
        x_list = []
        y_list = []
        for x,y in cell:
            x_list.append(x)
            y_list.append(y)
        if x_list[0] == x_list[1]:
            shipImage = pygame.transform.scale(shipImage,(30,60))
            shipImage = pygame.transform.rotate(shipImage, 90)
            DISPLAYSURF.blit(shipImage,ship_place)
        else:
            shipImage = pygame.transform.scale(shipImage,(30,60))
            DISPLAYSURF.blit(shipImage,ship_place)

    elif len(cell) == 3:
        x,y = min(list(cell))
        ship_place = ((y*30+pix)+30,(x*30)+30)
        x_list = []
        y_list = []
        for x,y in cell:
            x_list.append(x)
            y_list.append(y)
        if x_list[0] == x_list[1]:
            shipImage = pygame.transform.scale(shipImage,(30,90))
            shipImage = pygame.transform.rotate(shipImage, 90)
            DISPLAYSURF.blit(shipImage,ship_place)
        else:
            shipImage = pygame.transform.scale(shipImage,(30,90))
            DISPLAYSURF.blit(shipImage,ship_place)

    elif len(cell) == 4:
        x,y = min(list(cell))
        ship_place = ((y*30+pix)+30,(x*30)+30)
        x_list = []
        y_list = []
        for x,y in cell:
            x_list.append(x)
            y_list.append(y)
        if x_list[0] == x_list[1]:
            shipImage = pygame.transform.scale(shipImage,(30,120))
            shipImage = pygame.transform.rotate(shipImage, 90)
            DISPLAYSURF.blit(shipImage,ship_place)
        else:
            shipImage = pygame.transform.scale(shipImage,(30,120))
            DISPLAYSURF.blit(shipImage,ship_place)


def drawAllShip(ship, pix) :
    for k in ship.korabli:
        drawShip(DISPLAYSURF, k, pix)


def drawExplosion(display, ships,pix):
    for k in ships.korabli:
        for (x,y) in k.hitspace:
            explosion = pygame.image.load('data/explosion.png')
            place = ((y*30+pix)+33,(x*30)+25)
            DISPLAYSURF.blit(explosion,place)


def drawDeadShip(ship):
    for k in ship.korabli:
        if len(k.cells) == 0:
            drawShip(DISPLAYSURF,k,360)
        for (x,y) in k.hitspace:
            explosion = pygame.image.load('data/explosion.png')
            place = ((y*30+360)+33,(x*30)+25)
            DISPLAYSURF.blit(explosion,place)


def drawBum(ship,pix=0):
        for (x,y) in ship.bumspace:
            bumImage = pygame.image.load('data/bum.png')
            place = ((y*30+pix)+30,(x*30)+30)
            DISPLAYSURF.blit(bumImage,place)


def reDrawAll(ownship, enemyship, display):
    drawBoard()
    drawAllShip(ownship)
    drawBum(ownship)
    drawBum(enemyship,360)
    drawExplosion(display,ownship,0)
    drawExplosion(display,enemyship,360)
    drawDeadShip(enemyship)
    #drawDeadShip(ownship)

