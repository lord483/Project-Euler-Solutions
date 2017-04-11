'''
    Problem 501 - Eight Divisors

    The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24.
    The ten numbers not exceeding 100 having exactly eight divisors are :
            24, 30, 40, 42, 54, 56, 66, 70, 78 and 88.

    Let f(n) be the count of numbers not exceeding n with exactly eight divisors.
    You are given f(100) = 10, f(1000) = 180 and f(10**6) = 224427.

    Find f(10**12).
'''

from time import time
from numba import jit
import numpy as np


@jit
def getPrimes(n):
    q, r = divmod(n, 2)
    r = q + r
    seive = np.ones(r, dtype=bool)
    seive[0] = 0

    lim = int(n**0.5 / 2) + 1

    for i in range(1, lim + 1):
        p = 2 * i + 1
        if seive[i]:
            sp = 2 * i * (i + 1)
            seive[sp:r:p] = False

    def_prime = np.asarray([2])
    seived_primes = np.asarray(np.nonzero(seive)).flatten() * 2 + 1
    primes = np.concatenate((def_prime, seived_primes))
    return primes


@jit
def solve(n):
    res = 0

    # 1- Found 7th power of primes
    for p in primes:
        a = p**7
        if (a > n):
            break
        else:
            res += 1

    # 2- Next find 3rd Power X other primes
    l = len(primes)
    for i in range(l):
        a = primes[i]**3
        if a > n:
            break
        lim = n // a
        for j in range(l):
            if i == j:
                continue
            p = primes[j]
            if p > lim:
                break
            else:
                res += 1

    for i in range(l):
        a = primes[i]
        if a**3 > n:
            break
        for j in range(i + 1, l):
            b = primes[j]
            if a * b * b > n:
                break
            for k in range(j + 1, l):
                c = primes[k]
                p = a * b * c
                if p > n:
                    break
                else:
                    res += 1
    return res


if __name__ == "__main__":
    t0 = time()
    n = 10**12
    primes = getPrimes(n // 6)
    print("Number of primes {} , time taken : {:.2f} sec".format(len(primes), time() - t0))
    print(solve(n))
    print("Done , time taken : {:.2f} sec".format(time() - t0))
