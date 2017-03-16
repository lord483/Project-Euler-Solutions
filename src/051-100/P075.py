from collections import defaultdict
from numba import *

@jit
def compute_pytho():
    pytho = defaultdict(int)

    N = 1500000
    lim = int(N**0.5)

    print("Limiting search to : ", lim)

    for n in range(1,lim+1):
        for m in range(n+1,lim+1):
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            # c0 = c
            a0,b0 = min(a,b), max(a,b)
            a,b = a0,b0
            s0 = a+b+c
            i = 1
            s = s0
            # print(a,b,c)
            while s <= N:
                # print(a,b,c, s)
                p = pytho[s]
                if p == 0:
                    pytho[s] = a
                elif p != a:
                    pytho[s] = -1
                i += 1
                s,a = s0*i , a0*i
                # b,c = b0*i, c0*i


    return pytho

if __name__ == "__main__":
    pytho = compute_pytho()
    keys = list(pytho.keys())
    res = sum([1 for k in keys if pytho[k] > 0])
    print(res)
