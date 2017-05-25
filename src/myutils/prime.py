# A function to find out all the primes till the number n
#
# @Author : Subhendu Ranjan Mishra
#
# @Input : a positive intiger
# @Output : An array of intigers

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
def getPrimes2(n):
    arr = np.ones(n + 1, dtype=bool)
    arr[0], arr[1] = 0, 0
    for i in range(2, n + 1):
        if arr[i]:
            arr[i * i:n + 1:i] = False
    return arr.nonzero()[0]

if __name__ == '__main__':
    # Test Cases
    print("Testing the getPrimes function.")
    print("getPrimes2(18) : ", getPrimes2(18))
    print("getPrimes2(7) : ", getPrimes2(7))
    print("getPrimes2(25) : ", getPrimes2(25))
    print("getPrimes2(31) : ", getPrimes2(31))
    print()
    print("Now testing the getPrimes function for higher powers of 10")
    for power in range(1, 9):
        n = 10**power
        t0 = time()
        primes = getPrimes(n)
        print("1 - Computed for {:10d} ({}th power of 10), in {:03.5f} secs. number of primes : {:,}".format(
            n, power, time() - t0, len(primes)))

        # second function
        t0 = time()
        primes2 = getPrimes2(n)
        print("2 - Computed for {:10d} ({}th power of 10), in {:03.5f} secs. number of primes : {:,}".format(
            n, power, time() - t0, len(primes2)))
        # print(primes)
