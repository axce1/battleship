#import main

def vistrel(ship,x,y):
    x = (x-390)/30
    y = y/30 - 1
    print x,y
    ship.delFromKorabli(x,y)
