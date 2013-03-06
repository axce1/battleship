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
import xmpp
import pickle

login = "bship2@default.rs"
remote_user = "bship1@default.rs"
server = "default.rs"
password = "123456"

jid=xmpp.protocol.JID(login)
def msgparser(connect_object, message):
    global ownship, enemyship
    ownship = pickle.loads(message.getBody())
    draw.drawAllShip(ownship,0)
    enemyship = pickle.loads(message.getBody())
    print 'risuem hernyu'
    pygame.display.update()
#    draw.showStartScreen()


## connect
myclient = xmpp.Client(server) #, debug=[])
myclient.connect()
myclient.auth(jid.getNode(),password, 'BattleShip-JID2')

myclient.RegisterHandler('message', msgparser)

myclient.sendInitPresence()


#ownship = ships.workShip()
#enemyship = ships.workShip()

#OwnListShip = ownship.createListShips()
#EnemyListShip = enemyship.createListShips()

#draw.drawAllShip(ownship)

waitInput = True

while True:
    myclient.Process(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if (30 < mousey or mousey > 330) and (390 < mousex or mousex > 690):
                control.vistrel(ownship, enemyship, mousex, mousey)
                waitInput = False
        if not waitInput:
            control.compTurn(enemyship,ownship)
            waitInput = True
        pygame.display.update()
    sleep(0.05)

#while myclient.Process(1):
#    pass


