####
# first player using jid - bship1@default.rs
# second player using jid - bship2default.rs
####
# password for both jid 123456
####

import pickle
import xmpp
import pygame

import draw


login = "bship1@default.rs"
remote_user = "bship2@default.rs"
password = "123456"


def msgparser(connect_object, message):
    global ownship, enemyship, waitInput
    mess = pickle.loads(message.getBody())
    ownship =  mess[1]
    draw.drawAllShip(ownship)
    enemyship = mess[0]
    print (enemyship.bumspace)
    waitInput = mess[2]
    print waitInput
    print 'risuem hernyu'
    draw.reDrawAll(ownship, enemyship, draw.DISPLAYSURF)
    pygame.display.update()


def jinstance():
    #login = 'bship1@default.rs'
    #server = 'default.rs'
    #password = '123456'
    jid = xmpp.protocol.JID(login)
    client = xmpp.Client(jid.getDomain(), debug=[])
    client.connect()
    client.auth(jid.getNode(), password, 'BattleShip-JID1')
    client.RegisterHandler('message', msgparser)
    client.sendInitPresence()

    return client
