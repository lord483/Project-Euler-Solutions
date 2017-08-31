'''
    Problem 82 - Path sum: three ways

    A difficult version of P081 !
'''

import copy


def solve(size, ip):
    res = copy.deepcopy(ip)

    for j in range(1, size):

        for i in range(size):
            res[i][j] += res[i][j - 1]

        for i in range(1, size):
            res[i][j] = min(res[i][j], res[i - 1][j] + ip[i][j])

        for i in range(size - 2, -1, -1):
            res[i][j] = min(res[i][j], res[i + 1][j] + ip[i][j])

    return min(res[i][-1] for i in range(size))


if __name__ == "__main__":
    ip = []
    first_line = list(map(int, input().strip().split(",")))
    size = len(first_line)
    ip.append(first_line)
    for _ in range(size - 1):
        ip.append(list(map(int, input().strip().split(","))))
    print("size of the matrix : ", size)
    print(solve(size, ip))
