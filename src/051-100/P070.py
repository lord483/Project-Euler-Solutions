'''
    Problem 70 : Totient minimum (A more refined version of Problem # 69)
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
            # do not consider if divisible by small primes
            if p < 14:
                res = n >> 4
                n = 1
                break
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
    # N = 87109
    t0 = time()
    N = 10000000
    primes_list = getPrimes(int(N**0.5))

    a, r = 0, 10

    for i in range(10**3, N + 1):
        if i % (5 * 10**5) == 0:
            print("Now doing {:,}. Time Elapsed = {:.2f} secs".format(i, time() - t0))

        phi = get_phi(i)

        r1 = i / phi
        if r1 < r:
            s_i = "".join(sorted(str(i)))
            s_phi = "".join(sorted(str(phi)))
            if s_i == s_phi:
                a, r = i, r1

    print("Result : ", a, " , ratio :", r)
    print("Done in {:.3f} secs".format(time() - t0))
