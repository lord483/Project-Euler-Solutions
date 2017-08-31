'''
    Problem 87 - Prime power triples
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


if __name__ == "__main__":
    # print(getPrimes(29))
    N = 50 * (10**6)
    m = int(N**0.5)
    print("m : ", m)
    sol = set()
    primes = getPrimes(m)
    print("Number of primes = ", len(primes))

    sqrs = primes**2
    tripples = primes**3
    tripples = tripples[tripples < N]
    fourth = primes**4
    fourth = fourth[fourth < N]
    for s in sqrs:
        for t in tripples:
            for f in fourth:
                x = s + t + f
                if x < N:
                    sol.add(x)

    print(len(sol))
