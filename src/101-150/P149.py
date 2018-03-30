'''
Problem 149 : Searching for a maximum-sum subsequence
'''
import numpy as np
from time import time
from numba import jit


@jit
def Lagged_Fibonacci_Generator(m):
    a = np.zeros(m).astype(np.int32)
    for i in range(m):
        n = i + 1
        if n > 55:
            a[i] = ((a[i - 24] + a[i - 55] + 1000000) % 1000000) - 500000
        else:
            a[i] = ((100003 - 200003 * n + 300007 * (n**3)) % 1000000) - 500000

    return a


@jit
def max_subset_sum(arr):
    ms = 0
    s = 0
    for n in arr:
        s = max(0, s + n)
        ms = max(s, ms)
    return ms


@jit
def solve(mat):
    res = 0
    # find max sum of rows
    for i in range(2000):
        m = max_subset_sum(mat[i])
        res = max(m, res)

    # find max sum of columns
    for i in range(2000):
        m = max_subset_sum(mat[:, i])
        res = max(m, res)

    return res


if __name__ == "__main__":
    t0 = time()
    a = Lagged_Fibonacci_Generator(4000000)
    mat = a.reshape((2000, 2000))
    print(solve(mat))
    print("Done in {:.2f} secs".format(time() - t0))
