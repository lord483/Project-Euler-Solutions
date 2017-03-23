'''
    Problem 73 - Counting fractions in a range
'''

import numpy as np
from numba import jit

@jit
def getPrimes(n):
    arr = np.ones(n+1, dtype=bool)
    arr[0],arr[1] = False,False
    for i in range(2, n+1):
        if arr[i]:
            arr[i*i:n+1:i]= False
    return arr.nonzero()[0]


def phi(n):
    u = n//2 + n%2
    a = np.ones(u,dtype=bool)
    a[0] = False

    for p in primes:
        if p > u:
            break
        if n%p == 0 :
            a[p::p]= False


    found = a.nonzero()[0]
    l = n//3
    r = found[found>l]

    return len(r)

if __name__ == "__main__":
    N = 12000
    primes = getPrimes(N)
    res = 0
    for i in range(5,N+1):
        res += phi(i)

    print(res)
