'''
Problem 348  - Sum of a square and a cube

    Many numbers can be expressed as the sum of a square and a cube. 
    Some of them in more than one way.

    Consider the palindromic numbers that can be expressed as the sum of a square and a cube, 
    both greater than 1, in exactly 4 different ways.
    For example, 5229225 is a palindromic number and it can be expressed in exactly 4 different ways:

    2285^2 + 20^3
    2223^2 + 66^3
    1810^2 + 125^3
    1197^2 + 156^3

    Find the sum of the five smallest such palindromic numbers.

'''
import numpy as np
from itertools import product
from collections import defaultdict, Counter
from time import time
from numba import jit, vectorize, boolean, uint64


@vectorize([boolean(uint64)])
def is_palindrome(n):
    rev = 0
    a = n
    while a > 0:
        r = a % 10
        rev = (rev * 10) + r
        a = (a - r) // 10
    return n == rev


@jit
def solve():
    A = 3 * (10**4)
    B = 10**3
    numbers_a = np.arange(A, dtype="uint64")
    numbers_b = np.arange(B, dtype="uint64")
    sqrs = np.power(numbers_a, 2)
    cubes = np.power(numbers_b, 3)

    pal_sums = np.asarray([0]).astype("int64")

    for a in sqrs:
        sums = cubes + a
        new_pal_sums = sums[is_palindrome(sums)]
        pal_sums = np.hstack((pal_sums, new_pal_sums))

    pal_sums_counter = Counter(pal_sums)
    all_pal_sums_with_cnt = pal_sums_counter.items()

    # filtered = [k for k, v in all_pal_sums_with_cnt if v == 4]
    filtered = []
    for k, v in all_pal_sums_with_cnt:
        if v == 4:
            filtered.append(k)

    filtered.sort()

    print("Total number of such numbers : ", len(filtered))
    print("Result : ", filtered[:5], int(sum(filtered[:5])))


if __name__ == "__main__":

    t0 = time()
    solve()
    print("Time taken {:.2f} secs".format(time() - t0))
