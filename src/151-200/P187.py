'''
    Semiprimes !
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

if __name__ == "__main__":
    t0 = time()

    primes = getPrimes(10**8)
    print("\nNumber of primes = {} , time taken = {:.2f} sec".format(len(primes), time() - t0))

    l = len(primes)
    res = 0
    limit = 10**8

    for i in range(l):
        for j in range(i, l):
            if primes[i] * primes[j] < limit:
                res += 1
            else:
                break

    print("\nFinal Result : " , res)
    print("Total time taken : {:.2f} secs".format(time() - t0))
