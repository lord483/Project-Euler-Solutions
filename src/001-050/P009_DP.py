import sys
from math import sqrt


def get_pytho(n):
    # print(n)
    pytho = [-1 for i in range(n + 1)]
    mid = (n * 2) // 3
    m = (n // 3) + 1
    for a in range(2, m):
        mb = ((n - a) // 2) + 2
        for b in range(a + 1, mb):
            if a + b >= mid:
                break
            else:
                c = sqrt(a * a + b * b)
                s = int(a + b + c)
                if (c == int(c)) and (s <= n):
                    mul = a * b * c
                    if pytho[s] < mul:
                        pytho[s] = int(mul)
    return pytho


if __name__ == '__main__':

    t = int(input("# of test cases ? :"))
    inps = [0 for i in range(t)]
    for i in range(t):
        inps[i] = int(input("Case #" + str(i + 1) + " Enter the number : "))

    n = max(inps)

    pytho = get_pytho(n)

    for i in range(t):
        print(pytho[inps[i]])
