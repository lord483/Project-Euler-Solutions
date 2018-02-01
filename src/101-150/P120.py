'''
    Square remainders
    Problem 120
    Problem Satement :
        Let r be the remainder when (a−1)n + (a+1)n is divided by a2.

        For example, if a = 7 and n = 3, then r = 42: 63 + 83 = 728 ≡ 42 mod 49.
        And as n varies, so too will r, but for a = 7 it turns out that r_max = 42.

        For 3 ≤ a ≤ 1000, find ∑ r_max.
'''
from time import time


def rmax(a):
    '''
        Find the rmax for a
    '''
    res = 2 * a
    d = a * a
    for i in range(3, d + 1, 2):
        rem = (2 * i * a) % d
        res = max(res, rem)

    return res


def p120(n):

    res = 0

    for a in range(3, n + 1):
        t0 = time()
        r = rmax(a)
        res += r
        print("{} : {} . Time taken {:.3f} secs".format(a, r, time() - t0))

    return res


if __name__ == "__main__":
    n = 1000
    start_time = time()
    print(p120(n))
    print("Time taken {:.1f} secs".format(time() - start_time))
