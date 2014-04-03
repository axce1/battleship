from pygame.locals import *
from time import sleep
import draw
import ships
import control
import pygame
import sys


draw.showStartScreen()
draw.drawBoard()
###

from jabber import jinstance
import pickle


def msgparser(connect_object, message):
    global ownship, enemyship, waitInput
    mess = pickle.loads(message.getBody())
    ownship =  mess[1]
    draw.drawAllShip(ownship)
    enemyship = mess[0]
    waitInput = mess[2]
    print waitInput
    print 'risuem hernyu'
    draw.reDrawAll(ownship, enemyship, draw.DISPLAYSURF)
    pygame.display.update()


myclient = jinstance()
myclient.RegisterHandler('message', msgparser)

waitInput = False

while True:
    myclient.Process(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if (30<mousey<330) and (390<mousex<690):
                control.vistrel(ownship, enemyship, mousex, mousey)
                control.jabber_send(myclient, ownship, enemyship, wait=True)
                waitInput = False
        if not waitInput:
            #control.compTurn(enemyship,ownship)
            waitInput = True
        pygame.display.update()
    sleep(0.05)

#while myclient.Process(1):
#    pass


