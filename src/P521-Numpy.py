import numpy as np 
import math 

n = 1000000000000
m = int(n ** 0.5)

na = np.arange(n+1)

def isdiv(x,y):
    if (x>y) and (x % y == 0) :
        return y
    else:
        return x

vdiv = np.vectorize(isdiv)

if __name__ == "__main__":
    na = vdiv(na,2)
    for j in range(3,m+1,2):
        if na[j] == j :
            na = vdiv(na,j)
    na = na % 1000000000
    print(np.sum(na) % 1000000000  - 1)
