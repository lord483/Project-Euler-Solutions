'''
    Problem 93 - Arithmetic expressions
'''


def check(a, b, c, d):
    n = 0

    return n

if __name__ == "__main__":
    cnt = 0
    for a in range(1, 10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    n = check(a, b, c, d)
                    cnt += 1

    print(cnt)
