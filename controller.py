#import main

def vistrel(ship,x,y):
    x = (x-390)/30
    y = y/30 - 1
    print x,y
    if ship.delFromKorabli(x,y) == 0:
        print 'hvost'
