import math
n, d = 2, 5
a, b = 3, 7
limit = 10**6
while (True):
    x, y = n + a, d + b
    g = math.gcd(x, y)
    x, y = x // g, y // g
    if y > limit:
        break
    n, d = x, y

print(n, " ", d)
