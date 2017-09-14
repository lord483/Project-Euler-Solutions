'''
Problem 179  - Consecutive positive divisors

Find the number of integers 1 < n < 10**7,
    for which n and n + 1 have the same number of positive divisors.

For example:
    14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
'''


def solve(N):
    res = 0

    arr = [i for i in range(N + 1)]
    divs = [1 for i in range(N + 1)]

    # Seive to Precompute the Number of divisors

    for i in range(2, N):
        if arr[i] != i:
            continue

        divs[i] = 2
        start = i * 2
        for a in range(start, N + 1, i):
            val = arr[a]
            cnt = 0
            d, r = divmod(val, i)
            while r == 0:
                cnt += 1
                val = d
                d, r = divmod(val, i)

            arr[a] = val
            divs[a] *= (cnt + 1)

        # print(i, arr, divs)

    # find the Consecutive ints with same number
    for i in range(2, N):
        if divs[i] == divs[i + 1]:
            # print(i , divs[i])
            res += 1

    return res


if __name__ == "__main__":
    # N = int(input("Enter the limit : "))
    from time import time
    t0 = time()
    N = 10**7
    print(solve(N))
    print("Time taken : {:.2f} secs".format(time() - t0))
