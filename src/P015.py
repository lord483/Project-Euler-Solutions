# -*- coding: cp1252 -*-

'''
Problem 15

Lattice paths


Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''

def down(a):
    x=a[0]
    y=a[1]
    #print "in down " , x , " " , y 
    if y == 0 :
        return 0
    else:
        r = (x , y-1)
        if (x == 20) and (y-1 == 0):
            return 1
        else:
            return nxt(r)

def right(a):
    x=a[0]
    y=a[1]
    #print "in right " , x , " " , y
    if x == 20 :
        return 0
    else:
        r = (x + 1 , y)
        if (x+1 == 20) and (y == 0):
            return 1
        else:
            return nxt(r)


def nxt(a):
    x=a[0]
    y=a[1]
    r , d = 0 , 0
    #print "in nxt " , x , " " , y
    if x < 20:
        r=right(a)
    if y>0:
        d=down(a)
    return r+d

s = (0,20)
x= nxt(s)
print "result " , x 


