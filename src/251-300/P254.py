'''
Sums of Digit Factorials
Problem 254
'''
from time import time


def digit_sum(x):
    return sum((int(c) for c in str(x)))


def SF(n):
    digits = [int(c) for c in str(n)]
    f = 0
    for d in digits:
        f += fact[d]
    return digit_sum(f)


def p254(limit):
    g = [0 for i in range(limit)]

    i = 1
    while(not all(g)):
        sf = SF(i)
        if sf <= limit:
            if g[sf - 1] == 0:
                print(sf, i)
                g[sf - 1] = i
        i += 1

    return sum((digit_sum(x) for x in g))


if __name__ == "__main__":
    t0 = time()
    fact = [1 for _ in range(10)]
    for i in range(2, 10):
        fact[i] = fact[i - 1] * i

    res = p254(150)

    print("Result ", res)

    print("Time taken {:.2f} secs".format(time() - t0))
