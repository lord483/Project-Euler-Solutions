'''
    Special subset sums: optimum
'''

from itertools import combinations


def is_special(ip):
    n = len(ip)
    if len(set(ip)) < n:
        return False

    sums = [set() for _ in range(n)]
    maxi = [0 for _ in range(n)]
    mini = [0 for _ in range(n)]

    sums[1] = set(ip)
    maxi[1] = max(ip)
    mini[1] = min(ip)

    for size in range(2, n):
        for subset in combinations(ip, size):
            sub_sum = sum(subset)
            for si in range(1, size):
                if sub_sum < maxi[si]:
                    return False
            for si in range(1, size + 1):
                if sub_sum in sums[si]:
                    return False
            sums[size].add(sub_sum)
        maxi[size] = max(sums[size])

    return True


if __name__ == "__main__":
    res = 0
    in_file = "p105_sets.txt"
    with open(in_file) as f:
        for line in f:
            line = line.strip()
            if len(line) >= 13:
                ip = list(map(int, line.split(",")))
                if is_special(ip):
                    # print(ip)
                    res += sum(ip)
    print(res)
