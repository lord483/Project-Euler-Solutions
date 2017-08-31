'''
    Problem 78 - Coin partitions

    Let p(n) represent the number of different ways in which n coins can be separated into piles.
    For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

    Find the least value of n for which p(n) is divisible by one million.
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
