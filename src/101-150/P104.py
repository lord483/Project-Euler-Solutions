from time import time
import math

ratio = (math.sqrt(5) + 1) / 2


def power(x, y):
    sset = 10**30
    res = x
    for i in range(y - 1):
        res = res * x
        if res > sset:
            res = int(res) // 10
    return res


def solve():
    a, b = 1, 1
    k = 2
    n = 0
    tail = 10**9
    t0 = time()

    m, m1 = 100, 100
    base = 0

    while(True):
        k += 1
        n = a + b

        if k == m:
            base = n
        elif k > m:
            n = n % tail
            nset = set(str(n))
            if (len(nset) == 9) and ("0" not in nset):
                print(k, m1)
                multiple = power(ratio, k - m1)
                print("{:8f}".format(multiple))
                actual_n = int(base * multiple)

                head = str(actual_n)[:9]
                base = int(str(actual_n)[:20])
                m1 = k
                head_set = set(head)
                if (len(head_set) == 9) and ("0" not in head_set):
                    return k

        a, b = b, n

    return k

print(solve())
# print(n)
