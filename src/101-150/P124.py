'''
    Problem 124 : Ordered radicals
'''
from time import time
import numpy as np


def p124(n=10, k=4):
    seive = np.ones(n + 1)
    seive[0] = 0

    for i in range(2, n + 1):
        if seive[i] == 1:
            seive[i:n + 1:i] *= i

    l = [(i, rad) for i, rad in enumerate(seive)]
    l.sort(key=lambda x: x[1])
    return l[k][0]


if __name__ == "__main__":
    t0 = time()
    print(p124(n=10, k=4))
    print("Time taken : {:.2f} secs".format(time() - t0))

    t0 = time()
    print(p124(n=10, k=6))
    print("Time taken : {:.2f} secs".format(time() - t0))

    t0 = time()
    print(p124(n=100000, k=10000))
    print("Time taken : {:.2f} secs".format(time() - t0))
