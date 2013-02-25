import model

def vistrel(ship,x,y):
    x = (x-380)/30
    y = y/30 - 1
    print x,y
    for i in ship:
        if (y,x) in i.cells:
            print 'popal'
            i.tadish((y,x))
