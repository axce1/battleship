####
# first player using jid - bship1@default.rs
# second player using jid - bship2default.rs
####
# password for both jid 123456
####

import pickle
import xmpp

login = "bship1@default.rs"
remote_user = "bship2@default.rs"
password = "123456"

jid=xmpp.protocol.JID(login)

def msgparser(connect_object, message):
    str(message.getBody())


## connect
myclient = xmpp.Client(jid.getDomain()) #, debug=[])
myclient.connect()
myclient.auth(jid.getNode(),password, 'BattleShip-JID1')

#myclient.RegisterHandler('message', msgparser)

#myclient.sendInitPresence()


#while myclient.Process(1):
#    pass

## send message
m = pickle.dumps((9,0))
mymsg=xmpp.protocol.Message(remote_user, m)
myclient.send(mymsg)

