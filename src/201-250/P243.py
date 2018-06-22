'''
Resilience
Problem 243
'''

from fractions import Fraction
from itertools import combinations
from time import time

import numpy as np
from numba import jit

f0 = Fraction(15499, 94744)


@jit
def get_primes(n):
    arr = np.ones(n + 1, "?")
    arr[0], arr[1] = False, False
    for i in range(2, n + 1):
        if arr[i] == 1:
            arr[i * i:n + 1:i] = False
    return arr.nonzero()[0]


@jit
def get_prime_factors(d):
    factors = []
    a = d
    for p in primes:
        if (p * p) > a:
            if a > 1:
                factors.append(a)
            break
        elif a % p == 0:
            factors.append(p)
            while (a % p == 0):
                a = a // p

    return factors


def non_coprime_cnt(d, factors):
    '''
        Using Euler's Totient Function
    '''
    cnt = d
    for p in factors:
        cnt = (cnt // p) * (p - 1)

    return cnt


def non_coprime_cnt_1(d, factors):
    '''
        Using set inclusion exclusion principle
    '''
    cnt = 0
    nf = len(factors)
    action = -1
    for size in range(1, nf + 1):
        action = action * (-1)
        for f_set in combinations(factors, size):
            mul = 1
            for f in f_set:
                mul *= f
            s_cnt = (d // mul) - 1

            cnt += action * s_cnt

    return cnt


def compute_resilance(d):
    factors = get_prime_factors(d)

    if factors[0] == d:
        return Fraction(1)

    return Fraction(non_coprime_cnt(d, factors), d - 1)


if __name__ == "__main__":

    primes = get_primes(10**4)
    print("Primes computed")

    # Test
    # print(compute_resilance(10))
    # print(compute_resilance(11))
    # print(compute_resilance(12))
    # print(compute_resilance(20))

    x = 2 * 3 * 5 * 7 * 11 * 13 * 17
    print("x {:,}".format(x))
    step = 10 ** 8
    next_stop = step
    min_i, min_f = 0, Fraction(1, 1)

    for i in range(x, 10**10, x):
        f = compute_resilance(i)

        if f < min_f:
            min_f = f
            min_i = i

        if f < f0:
            print("\n" + "=" * 80)
            print("solution found !!! ", i)
            print("Found : {:,} !!!. Ressilance factor {:.15f}".format(
                i, float(f)))
            print("=" * 80 + "\n")
            break

        if i >= next_stop:
            print("Current i: {:,} ,required factor: {:.15f} min_i: {:,} min_f : {:.15f} ".format(
                i, float(f0), min_i, float(min_f)))
            next_stop = i + step

    print("Done")
