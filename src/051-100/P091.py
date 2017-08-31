'''
    Problem 91 -Right triangles with integer coordinates
'''


def is_right(a, b, c):
    d1 = (a[0] - b[0])**2 + (a[1] - b[1])**2
    d2 = (a[0] - c[0])**2 + (a[1] - c[1])**2
    d3 = (c[0] - b[0])**2 + (c[1] - b[1])**2

    d1, d2, d3 = sorted([d1, d2, d3])
    if d1 > 0:
        if (d3 == d1 + d2):
            return True
    return False


if __name__ == "__main__":
    res = 0
    for x1 in range(51):
        for y1 in range(51):
            for x2 in range(51):
                for y2 in range(51):
                    if is_right((x1, y1), (x2, y2), (0, 0)):
                        res += 1

    print(res)
    print(res // 2)
