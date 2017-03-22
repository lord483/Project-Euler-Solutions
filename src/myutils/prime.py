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
    q,r = divmod(n,2)
    r = q+r
    seive = np.ones(r)
    seive[0] = 0

    lim = int(n**0.5 / 2) + 1

    for i in range(1, lim + 1):
        p = 2 * i + 1
        if seive[i]:
            sp = 2 * i * (i + 1)
            while(sp < r):
                seive[sp] = 0
                sp = sp + p

    def_prime = np.asarray([2])
    seived_primes = np.asarray(np.nonzero(seive)).flatten()*2 + 1
    primes = np.concatenate((def_prime, seived_primes))
    return primes


if __name__ == '__main__':
    # Test Cases
    print("Testing the getPrimes function.")
    print("getPrimes(18) : ", getPrimes(18))
    print("getPrimes(7) : ", getPrimes(7))
    print("getPrimes(25) : ", getPrimes(25))
    print("getPrimes(31) : ", getPrimes(31))
    print()
    print("Now testing the getPrimes function for higher powers of 10")
    for power in range(1, 10):
        n = 10**power
        t0 = time()
        primes = getPrimes(n)
        print("Computed for {:10d} ({}th power of 10), in {:03.5f} secs. number of primes : {:,}".format(
            n, power, time() - t0, len(primes)))
        # print(primes)
