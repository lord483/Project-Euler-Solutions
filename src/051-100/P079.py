'''
    Passcode derivation
    Problem 79 : https://projecteuler.net/problem=79
'''
from collections import defaultdict


def dfs(key):
    global visited
    nodes = g[key]
    for node in nodes:
        if node not in visited:
            visited.add(node)
            dfs(node)


def find_all_ends(x):
    global visited
    visited = set()
    keys_ = keys[x]
    for key in keys_:
        dfs(key)
    return [v // 100 if v >= 100 else 0 for v in visited]


def gc(z):
    if z == 0:
        return len(keys[z])
    else:
        return z * 100 + len(keys[z])


def check(x, y):
    if y not in keys:
        k = gc(y)
        keys[y] = [k]
        g[k] = []

    if x not in keys:
        k = gc(x)
        keys[x] = [k]
        g[k] = keys[y][:]
    else:
        ends = find_all_ends(x)
        if y not in set(ends):
            nk = gc(x)
            keys[x].append(nk)
            g[nk] = keys[y][:]


def add(a, b, c):
    check(b, c)
    check(a, b)
    return

if __name__ == "__main__":
    g = defaultdict(list)
    keys = defaultdict(list)

    ip = []
    with open("p079_keylog.txt") as f:
        for line in f:
            ip.append([int(c) for c in line.strip()])
    print(len(ip))
    for a, b, c in ip:
        add(a, b, c)

    _keys = list(g.keys())
    _keys.sort()
    for k in _keys:
        print(k, " : ", g[k])
    print("Result ", len(g.keys()))
