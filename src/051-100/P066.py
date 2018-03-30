# Find a fraction that closely matches sqrt(d)
# The numerator and denominator are the solution

# Look for Pell's equation in Google !


def solve(D):
    x1, y1 = 0, 1
    x2, y2 = 1, 0

    while (True):

        x, y = x1 + x2, y1 + y2
        t = x * x - D * y * y
        if t == 1:
            return x

        if t > 0:
            x2, y2 = x, y
        else:
            x1, y1 = x, y


if __name__ == "__main__":
    N, R = 0, 0
    for i in range(2, 1001):
        sqrt = int(i**0.5)
        if sqrt * sqrt == i:
            # No solution for square numbers
            continue

        r = solve(i)
        # print("{:04d} {}".format(i,r))
        if r > R:
            N, R = i, r

    print("Largest Value Found for {} is {}".format(N, R))
