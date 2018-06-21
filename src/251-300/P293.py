'''
    Problem 293 - Pseudo-Fortunate Numbers
'''

import numpy as np
from time import time
from numba import jit
# MAX = 10 * 5
MAX = 10**9


@jit
def get_primes(n):
    arr = np.ones(n + 1, "b")
    arr[0], arr[1] = False, False
    for i in range(2, n + 1):
        if arr[i] == 1:
            arr[i * i:n + 1:i] = False
    return arr.nonzero()[0]


def get_all_fortunates():
    pow_of_2 = [2]
    p = 2
    while(True):
        p = p * 2
        if p < MAX:
            pow_of_2.append(p)
        else:
            break
    fortunates.update(pow_of_2)
    print("Pow of 2 : ", pow_of_2)

    prev_list = pow_of_2
    for prime in primes[1:]:
        # print("Trying prime : ", prime)
        new_list = []
        for a in prev_list:
            n = a
            while(True):
                n = n * prime
                if n < MAX:
                    new_list.append(n)
                else:
                    break
        if len(new_list) == 0:
            break

        fortunates.update(new_list)
        prev_list = new_list


def solve_p293():
    res = set()
    j = 0

    for f in fortunates_list:
        while primes[j] <= f + 1:
            j += 1

        m = primes[j] - f
        res.add(m)

    return sum(res)


if __name__ == "__main__":
    t0 = time()
    primes = get_primes(int(MAX * 1.2))
    print("Tiem taken {:.2f} secs, num of primes {}".format(
        time() - t0, primes.shape[0]))

    fortunates = set()
    get_all_fortunates()

    fortunates_list = list(fortunates)
    fortunates_list.sort()
    print("Fortunates found. # ", len(fortunates_list))
    # print(fortunates_list)

    res = solve_p293()

    print(res)
