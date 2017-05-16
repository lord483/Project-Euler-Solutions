'''
    Triangle containing Origin
'''


def zero_on_line(xa, ya, xb, yb):

    d = ((xa - xb)**2 + (ya - yb)**2)**0.5
    d1 = (xa**2 + ya**2)**0.5
    d2 = (xb**2 + yb**2)**0.5

    if d == d1 + d2:
        return True

    return False


def does_intersect(xa, ya, xb, yb):
    '''
        check if the line x=y interesect this line segment
    '''
    m = (ya - yb) / (xa - xb)
    c = ya - m * xa

    if m == 1:
        return 0

    p = c / (1 - m)   # The intersection is at (p,p)

    if p <= 0:
        return 0

    if p == xa:
        if (p > ya) == (p < yb):
            return 1
        else:
            return 0
    elif p == ya:
        if (p > xa) == (p < xb):
            return 1
        else:
            return 0
    elif ((p > xa) == (p < xb)) and ((p > ya) == (p < yb)):
        return 1
    else:
        return 0


def origin(x1, y1, x2, y2, x3, y3):
    '''
        Check if Origin (0,0) in within the triangle.
    '''

    if (x1 == 0) and (y1 == 0):
        return False
    elif (x2 == 0) and (y2 == 0):
        return False
    elif (x3 == 0) and (y3 == 0):
        return False
    elif (y1 < 0) and (y2 < 0) and (y3 < 0):
        return False
    elif (y1 > 0) and (y2 > 0) and (y3 > 0):
        return False
    elif (x1 < 0) and (x2 < 0) and (x3 < 0):
        return False
    elif (x1 > 0) and (x2 > 0) and (x3 > 0):
        return False

    if zero_on_line(x1, y1, x2, y2):
        return False
    elif zero_on_line(x1, y1, x3, y3):
        return False
    elif zero_on_line(x3, y3, x2, y2):
        return False

    i1 = does_intersect(x1, y1, x2, y2)
    i2 = does_intersect(x1, y1, x3, y3)
    i3 = does_intersect(x3, y3, x2, y2)

    if sum([i1, i2, i3]) == 1:
        return True

    return False

if __name__ == "__main__":
    input_file = "./p102_triangles.txt"
    res = 0
    with open(input_file) as fin:
        for line in fin:
            x1, y1, x2, y2, x3, y3 = map(int, line.split(","))
            if origin(x1, y1, x2, y2, x3, y3):
                res += 1

    print(res)
