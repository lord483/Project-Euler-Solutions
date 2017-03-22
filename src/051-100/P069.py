'''
    Problem 69 : Totient maximum
'''
from time import time
from numba import jit
import numpy as np


@jit
def getPrimes(n):
    q, r = divmod(n, 2)
    r = q + r
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
    seived_primes = np.asarray(np.nonzero(seive)).flatten() * 2 + 1
    primes = np.concatenate((def_prime, seived_primes))
    return primes


@jit
def get_phi(n):
    if n in primes_list:
        return n - 1

    res = n
    for p in primes_list:
        r = n % p
        if r == 0:
            while r == 0:
                n = n // p
                r = n % p

            res = res // p
            res = res * (p - 1)
        elif p * p > n:
            break

    if n > 1:
        res = res // n
        res = res * (n - 1)

    return res


if __name__ == "__main__":
    t0 = time()
    N = 1000000
    primes_list = getPrimes(int(N**0.5))
    print("Primes computed in {:.3f} secs".format(time() - t0))
    a, r = 0, 0
    for i in range(2, N + 1):
        phi = get_phi(i)
        # print(i," ", phi)
        r1 = i / phi
        if r1 > r:
            a, r = i, r1

    print("Result : ", a, " , ratio :", r)
    print("Done in {:.3f} secs".format(time() - t0))
