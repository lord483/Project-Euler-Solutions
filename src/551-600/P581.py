# -*- coding: utf-8 -*-
# @Author: author
# @Date:   2017-01-19 13:25:20
# @Last Modified by:   Subhendu Ranjan Mishra
# @Last Modified time: 2017-01-19 13:55:05

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
if __name__ == "__main__":
    res = 0
    cnt = 0
    for n in range(1, 10**8 + 1):
        # n = int(input("Enter a Number : "))
        m = n * (n + 1)
        m = m >> 1

        # print(" M : ", m)

        factors = [0 for p in primes]

        for i, p in enumerate(primes):
            q, r = divmod(m, p)
            while r == 0:
                factors[i] += 1
                m = q
                q, r = divmod(m, p)
            if m == 1:
                break

        if m == 1:
            res += n
            cnt += 1

        if n % 1000000 == 0:
            print("{:,}  {:,} {:,}".format(n, cnt, res))
        # print("Reamining M : ", m)
        # for i, f in enumerate(factors):
        #     if f > 0:
        #         p = primes[i]
        #         print(p, f, p**f)

    print("Count ", cnt)
    print(res)
