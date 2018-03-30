'''
    Problem 123 : Square remainders

    Problem Satement :
        Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and
        let r be the remainder when (pn − 1)^n + (pn + 1)^n is divided by pn^2.

        For example, when n = 3, p3 = 5, and 4^3 + 6^3 = 280 ≡ 5 mod 25.

        The least value of n for which the remainder first exceeds 10^9 is 7037.

        Find the least value of n for which the remainder first exceeds 10^10.
'''
from time import time
import numpy as np


def get_primes(n):
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


def get_rem(p, n):
    '''
        Find  [ (p-1)^n + (p+1)^n ] % p^2
    '''
    rem = 2 * p
    d = p * p
    if n % 2 == 1:
        rem = (2 * n * p) % d

    return rem


def p123(m=10**10):
    primes = get_primes(10**6)

    n = 0
    res = 0
    while (True):
        n += 1
        p = primes[n - 1]
        rem = get_rem(p, n)
        if rem > m:
            break

    return n


if __name__ == "__main__":
    m = 10**10
    start_time = time()
    print(p123(m))
    print("Time taken {:.1f} secs".format(time() - start_time))
