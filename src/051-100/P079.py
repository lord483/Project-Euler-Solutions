'''
    Passcode derivation
    Problem 79 : https://projecteuler.net/problem=79
'''
# Solved it by hand

if __name__ == "__main__":
    g = defaultdict(list)
    keys = defaultdict(list)

    _ip = set()
    with open("p079_keylog.txt") as f:
        for line in f:
            _ip.add(int(line.strip()))
    ip = sorted(list(_ip))
    print(ip)
    print(len(ip))
