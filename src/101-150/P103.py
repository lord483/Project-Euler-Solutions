'''
    Special subset sums: optimum
'''

from itertools import combinations


def special_slower(t, n):
    sums = set()
    for i in t:
        old_sums = list(sums)
        for j in old_sums:
            if i + j in sums:
                return False
            sums.add(i + j)
        sums.add(i)

    return True


def special(t, n):
    for i in range(1, (n // 2)):
        if sum(t[:i + 1]) <= sum(t[-i:]):
            return False

    s = sum(t)
    sums = set()

    for i in range(2, (n // 2) + 1):
        # print(i)
        for t1 in combinations(t, i):
            # print(t,t1)
            s1 = sum(t1)
            s2 = s - s1
            if s1 == s2:
                return False
            if s1 in sums:
                return False
            else:
                sums.add(s1)
            if i * 2 < n:
                if s2 in sums:
                    return False
                else:
                    sums.add(s2)

    return True


if __name__ == "__main__":
    # Let's try 5 first
    l = [i for i in range(20, 46)]
    res = 10**6
    res_t = None
    m = 7
    for t in combinations(l, m):
        # print(t)
        if special(t, m):
            if sum(t) < res:
                res = sum(t)
                res_t = t
                print(res, t)

    print(res_t)
