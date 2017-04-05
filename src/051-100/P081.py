'''
    Problem 81 - Path sum: two ways
'''


def solve(size, ip):
    res = ip.copy()
    for i in range(size):
        for j in range(size):
            if i == 0:
                if j > 0:
                    res[i][j] += res[i][j - 1]
            else:
                if j == 0:
                    res[i][j] += res[i - 1][j]
                else:
                    res[i][j] += min(res[i - 1][j], res[i][j - 1])

    return res[-1][-1]

if __name__ == "__main__":
    ip = []
    first_line = list(map(int, input().strip().split(",")))
    size = len(first_line)
    ip.append(first_line)
    for _ in range(size - 1):
        ip.append(list(map(int, input().strip().split(","))))
    print("size of the matrix : ", size)
    print(solve(size, ip))
