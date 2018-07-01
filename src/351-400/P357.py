import numpy as np
from numba import jit
from time import time


@jit
def getPrimes(n):
    arr = np.ones(n + 1, dtype=bool)
    arr[0], arr[1] = 0, 0
    for i in range(2, n + 1):
        if arr[i]:
            arr[i * i:n + 1:i] = False
    return arr


@jit
def solve():
    t1 = time()
    is_prime = getPrimes(MAX + 1)
    print("Primes claculated. ")
    print("Time taken {:.2f} secs".format(time() - t1))

    res = 3
    for n in range(6, MAX + 1, 4):
        lim = int(n**0.5) + 1
        good = True
        for i in range(1, lim):
            if n % i == 0:
                j = n // i
                if not is_prime[i + j]:
                    good = False
                    break

        if good:
            res += n
            # print(n)
    return res


if __name__ == "__main__":
    MAX = 10 ** 8
    t0 = time()
    res = solve()
    print("\nResult : ", res)
    print("Total Time taken {:.2f} secs".format(time() - t0))
