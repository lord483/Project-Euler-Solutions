'''
    Problem 58 -  Spiral primes
'''
from itertools import *
from array import array
from time import time


def getPrimes(n):
    r = n // 2
    # plist = list(islice(repeat(1), r + 1))
    plist = array("I", islice(repeat(1), r + 1))
    plist[0] = 0

    lim = int((n**0.5) / 2 + 1)

    for i in range(1, lim + 1):
        p = 2 * i + 1

        if plist[i]:
            sp = 2 * i * (i + 1)
            while (sp <= r):
                plist[sp] = 0
                sp = sp + p

    primes = array("l", [2] + [(2 * i + 1) for i in range(r) if plist[i]])
    return primes


def is_prime(n):
    l = int(n**0.5)
    for p in primes:
        if n % p == 0:
            return False
        elif p > l:
            return True
    return True


if __name__ == "__main__":
    limit = 10**7
    t0 = time()
    primes = getPrimes(limit)
    print("Number of pimes = ", len(primes))
    print("time taken = {:.2f} secs".format(time() - t0))
    # let's compute
    ratio = 0.1
    total_diag = 5
    primes_in_diag = 3
    prime_ratio = primes_in_diag / total_diag
    side_length = 3
    while prime_ratio > ratio:
        side_length += 2
        total_diag += 4
        b = side_length * side_length
        d = side_length - 1
        new_numbers = [b - (i * d) for i in range(1, 4)]
        for n in new_numbers:
            if is_prime(n):
                primes_in_diag += 1
        prime_ratio = primes_in_diag / total_diag

    print("Final result : {} , ratio={:.6f}".format(side_length, prime_ratio))
