'''
The Ackermann function
Problem 282
'''
import sys
# sys.setrecursionlimit(5000)
from time import time
# from numba import jit

dp = [[0 for _ in range(1000000)] for _ in range(7)]


# @jit
def A(m, n):
    if dp[m][n] > 0:
        return dp[m][n]

    if m == 0:
        return n + 1
    elif n == 0:
        r = A(m - 1, 1)
    else:
        r1 = A(m, n - 1)
        r = A(m - 1, r1)

    dp[m][n] = r
    return r


if __name__ == "__main__":
    t0 = time()
    r = A(1, 0)
    print("A(1,0) = {:5d} . Time taken {:.3f} secs".format(r, time() - t0))
    t0 = time()
    r = A(2, 2)
    print("A(2,2) = {:5d} . Time taken {:.3f} secs".format(r, time() - t0))
    t0 = time()
    r = A(3, 4)
    print("A(3,4) = {:5d} . Time taken {:.3f} secs".format(r, time() - t0))

    MOD = 14**8
    t0 = time()
    res = 0
    for i in range(1, 7):
        t1 = time()
        r = A(i, i)
        res += r
        res = res % MOD
        print("A({},{}) = {} . Time taken {:.3f} secs".format(
            i, i, r, time() - t1))

    print("Final result = {} . Time taken {:.3f} secs".format(res, time() - t0))
