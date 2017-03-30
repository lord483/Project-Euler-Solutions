'''
    Problem 77 : Prime summations

    Desc :
        It is possible to write ten as the sum of primes in exactly five different ways:

        7 + 3
        5 + 5
        5 + 3 + 2
        3 + 3 + 2 + 2
        2 + 2 + 2 + 2 + 2

        What is the first value which can be written as the sum of primes in over five thousand different ways?
'''
import numpy as np
from numba import jit


@jit
def solve(n, m):
    res = 0
    a = np.ones(n + 1).astype(np.uint32)
    b = np.ones(n + 1).astype(np.uint32)

    for i in range(2, n + 1):
        for j in range(1, n + 1):
            if j < i:
                b[j] = a[j]
            else:
                b[j] = (a[j] + b[j - i]) % m

        if b[i] % m == 0:
            res = i
            break

        a = b.copy()
        b = np.ones(n + 1).astype(np.uint32)

    return res

if __name__ == "__main__":
    lim = 100000
    print(solve(lim, 10**6))
    # print(solve(lim,10**6))
