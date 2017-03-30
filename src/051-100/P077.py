'''
    Problem 77 : Prime summations

    Desc :
        It is possible to write ten as the sum of primes in exactly five different ways:

        7 + 3
        5 + 5
        5 + 3 + 2
        3 + 3 + 2 + 2
        2 + 2 + 2 + 2 + 2

        What is the first value which can be written as the sum of primes in over five thousand different ways?
'''
import numpy as np
from numba import jit


@jit
def getPrimes(n):
    arr = np.ones(n + 1, dtype=bool)
    arr[0], arr[1] = 0, 0
    for i in range(2, n + 1):
        if arr[i]:
            arr[i * i:n + 1:i] = False
    return arr.nonzero()[0]


def compute_sum_matrix(n, primes):
    arr = np.zeros((len(primes), n + 1))
    p = primes[0]
    arr[0, p:n + 1:p] = 1

    for i in range(1, len(primes)):
        p = primes[i]
        arr[i, 0] = 1
        for j in range(1, n + 1):
            if j < p:
                arr[i, j] = arr[i - 1, j]
            else:
                arr[i, j] = arr[i - 1, j] + arr[i, j - p]

    return arr

if __name__ == "__main__":
    n = 100
    primes = getPrimes(n)
    print("Number of primes : ", len(primes))
    sum_matrix = compute_sum_matrix(n, primes)
    # print(sum_matrix)
    res = n
    for i, row in enumerate(sum_matrix):
        for j, value in enumerate(row):
            if value > 5000:
                if j < res:
                    res = j
    print(res)
