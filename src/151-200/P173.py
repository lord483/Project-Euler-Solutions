'''
    Problem 173 : Using up to one million tiles how many different "hollow" square laminae can be formed?
'''
from time import time


def count(i, N):
    if ((i * i) <= N):
        if i % 2 == 0:
            return i // 2 - 1
        else:
            return i // 2

    cnt, tiles = 0, 0
    for j in range(i // 2 + 1):
        k = i - (j * 2)
        tiles += (4 * k - 4)
        if tiles <= N:
            cnt += 1
        else:
            break

    return cnt


def solve_p173(N):
    res = 0

    limit = (N + 4) // 4

    for i in range(3, limit + 1):
        r = count(i, N)
        res += r
        # print(i,r)

    return res


if __name__ == "__main__":
    # N = int(input("Enter the limit : "))
    t0 = time()
    N = 1000000
    r = solve_p173(N)
    print("Result : ", r)
    print("Time taken : {:.3f} secs".format(time() - t0))
