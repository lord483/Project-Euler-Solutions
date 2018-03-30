'''
	Problem 549 - Divisibility of factorials

	The smallest number m such that 10 divides m! is m=5.
	The smallest number m such that 25 divides m! is m=10.

	Let s(n) be the smallest number m such that n divides m!.

	So s(10)=5 and s(25)=10.

	Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
	S(100)=2012.

	Find S(10^8).
'''
import math
from utils import prime

limit = 100

# limit = 100000000


def getDiv(n):
    global plist
    res = []
    l = math.sqrt(n)
    for p in plist:
        if p > n:
            res.append(n)
            break
        while (n % p == 0):
            res.append(p)
            n = n // p
    return res


def solve(n):
    global plist
    if n in plist:
        return n
    else:
        div = getDiv(n)
        dd = {}
        for d in div:
            if d in dd:
                dd[d] += 1
            else:
                dd[d] = 1
        res = []
        for x, y in dd.items():
            r = x * y
            pn = 1
            py = 2
            while py * 2 <= y:
                py = py * y
                pn = pn + 1
            ny = py
            dy = y - ny

            res.append(r)

        return max(res)


if __name__ == "__main__":
    global plist
    plist = prime.getPrimes(limit)
    print(len(plist))
    res = 14
    for i in range(6, limit + 1):
        r = solve(i)
        res = res + r
        print("i={0} , r={1}".format(i, r))
    print("Final result is : {0}".format(res))
