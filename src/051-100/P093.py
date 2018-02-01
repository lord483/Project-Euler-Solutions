'''
    Problem 93 - Arithmetic expressions
'''
MAX = 6 * 7 * 8 * 9


def check(a, b, c, d):
    res = [0 for i in range(MAX + 1)]
    res[0] = 1

    parms = [a, b, c, d]
    for i in range(4):
        keep = parms[i]
        rem = parms[:i] + parms[i + 1:]
        for p2 in check3(*rem):
            final_values = check2(keep, p2)
            for fv in final_values:
                if (fv > 0) and (fv == int(fv)):
                    res[int(fv)] = 1

    n = 0
    for i in range(MAX + 1):
        if res[i] == 0:
            n = i - 1
            break

    return n


def check3(x, y, z):
    parms = [x, y, z]
    res = []
    for i in range(3):
        keep = parms[i]
        rem = parms[:i] + parms[i + 1:]
        for p1 in check2(*rem):
            res.extend(check2(keep, p1))

    return res


def check2(x, y):
    res = [x + y, x - y, y - x, x * y]
    if x != 0:
        res.append(y / x)
    if y != 0:
        res.append(x / y)
    return res


if __name__ == "__main__":
    sol = []
    for a in range(1, 7):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    combined = a * 1000 + b * 100 + c * 10 + d
                    n = check(a, b, c, d)
                    print("For {} n is {}".format(combined, n))
                    sol.append((combined, n))

    sol.sort(key=lambda x: x[1], reverse=True)
    print(len(sol))
    print(sol[0])
