'''
    Problem 85 - Counting rectangles
'''


def num_of_rects(n, m):
    res = 0
    for x in range(1, n + 1):
        nx = n + 1 - x
        for y in range(1, m + 1):
            ny = m + 1 - y
            res += (x * y)

    return res


if __name__ == "__main__":
    # tests
    print("1x1 : ", num_of_rects(1, 1))
    print("1x2 : ", num_of_rects(1, 2))
    print("2x2 : ", num_of_rects(2, 2))
    print("2x3 : ", num_of_rects(2, 3))

    lim = 2 * (10**6)
    res = 0
    diff = lim
    for i in range(1, 100):
        for j in range(i, 100):
            r = num_of_rects(i, j)
            d = abs(lim - r)
            if d < diff:
                diff = d
                res = i * j

    print("diff :", diff, " res :", res)
