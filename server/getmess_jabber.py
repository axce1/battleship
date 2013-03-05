####
# first player using jid - bship1@default.rs
# second player using jid - bship2default.rs
####
# password for both jid 123456
####

import xmpp

login = "bship2@default.rs"
remote_user = "bship1@default.rs"
server = "default.rs"
password = "123456"

jid=xmpp.protocol.JID(login)
a = set([(1,1)])
def msgparser(connect_object, message):
    mess = str(message.getBody())
    print a
    print set([mess])


## connect
myclient = xmpp.Client(server) #, debug=[])
myclient.connect()
myclient.auth(jid.getNode(),password, 'BattleShip-JID2')

myclient.RegisterHandler('message', msgparser)

myclient.sendInitPresence()

## send message
#m ='message was send from 2 to 1'
#mymsg=xmpp.protocol.Message(remote_user, m, 'chat')
#myclient.send(mymsg)
while myclient.Process(1):
    pass

