'''
    Problem 112 - Bouncy numbers
'''


def is_bouncy(n):
    l = list(map(int, str(n)))

    increasing = False
    i = 0
    while (l[i + 1] == l[i]):
        i += 1
        if i == len(l) - 1:
            return False

    if l[i + 1] > l[i]:
        increasing = True

    d0 = l[i]

    for d in l[i + 1:]:
        if d == d0:
            continue
        elif d > d0:
            if not increasing:
                return True
        else:
            if increasing:
                return True
        d0 = d

    return False


if __name__ == "__main__":
    ratio = 0
    cnt = 0
    i = 100
    # while(i < 1000):
    while (ratio < 0.99):
        i = i + 1
        # print(i,is_bouncy(i))
        if is_bouncy(i):
            cnt += 1
        ratio = cnt / i

    print(i, cnt)
