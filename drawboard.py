from pygame.locals import *
import pygame
import ships

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


#class Ship():
    #'''class for work with ships '''

    #def drawship(self,arg,deck):

        #'''draw own ships. arg - how much ships we need'''

        #for i in range(arg):

            #x = random.randrange(0,300,30)
            #y = random.randrange(0,300,30)

            #rect_1_rect = Rect((x+32,y+32),(28,28))

            #print x/30 , y/30

            #if deck == 1:
                #rect_1_rect = Rect((x+32,y+32),(28,28))
                #pygame.draw.rect(DISPLAYSURF,OWNSHIPCOLOR,rect_1_rect,0)

            #elif deck == 2:
                #rect_1_rect = Rect((x+32,y+32),(28,58)) # vertical ship
                #pygame.draw.rect(DISPLAYSURF,OWNSHIPCOLOR,rect_1_rect,0)


drawBoard(0)
drawBoard(350)
a = ships.Korablic()

def drawAllKorablics(koralblics):
    for kor in range(koralblics):
        a.draw(DISPLAYSURF,OWNSHIPCOLOR)


drawAllKorablics(20)

while True:
    pygame.display.update()

