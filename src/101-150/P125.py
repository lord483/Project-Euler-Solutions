'''
    Palindromic sums of consecutive squares
'''
from time import time


def solve(n):
    def is_palli(x):
        return x == x[::-1]

    res = 0
    lim = int(n**0.5) + 1
    sqrs = [i * i for i in range(1, lim + 1)]

    s = 0
    l = len(sqrs)
    found = set()

    for i in range(l - 1):
        s = sqrs[i]
        for j in range(i + 1, l):
            s += sqrs[j]
            if s > n:
                break
            elif is_palli(str(s)):
                if s not in found:
                    res += s
                    found.add(s)

    return res


if __name__ == '__main__':
    t0 = time()
    print(solve(10**8))
    print("Time taken = {:.2f} secs".format(time() - t0))
