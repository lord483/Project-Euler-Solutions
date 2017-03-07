
from math import sqrt

penta = []
max_l = 10001

'''
def penta_num(n):
    p = (3*n - 1) *n /2
    p = int(p)
    return p

penta = list(map(penta_num,range(1,max_l)))

pmax = penta[-1]
print(" First step complete : " , pmax)
print(penta[:20])
'''


def bin_search(a, high, low=0):
    f = 0
    #print('in penta for ' , a , high)
    #print("penta now = ", penta)

    while(True):
        mid = (high + low) // 2
        #print("high = ", high, " mid = " ,mid ," low=", low)
        if penta[mid] == a:
            f = 1
            break
        if (high == low) or (high < low):
            break
        elif penta[mid] > a:
            high = mid
        else:
            low = mid + 1

    return f

pl = 500

for i in range(1, max_l):
    pi = int(((3 * i - 1) * i) / 2)
    penta.append(pi)
    f = 0
    # print(i)
    for j in range(i):
        pj = penta[j]
        d = pi - pj

        # if (d in penta):
        if bin_search(d, i - 1) > 0:
            s = pi + pj
            #print("temp found : ",i+1,' ', pi,' ', j+1,' ',pj,' ', d , " ",s)
            sq = sqrt(24 * s + 1)
            if sq == int(sq):
                n = (1 + sq) / 6
                if n == int(n):
                    print("found : ", i + 1, ' ', pi, ' ', j + 1, ' ', pj, ' ', d, " ", s, " ", n)
                    f = 1
                    break
    if i == pl:
        print("Now at : ", i)
        pl = pl + 500

    if f == 1:
        break
'''
'''
