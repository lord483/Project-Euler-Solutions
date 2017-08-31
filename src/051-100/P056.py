'''
Powerful digit sum
Problem 56

A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?   '''

maxs = 0


def sum_digit(a):
    s = 0
    for i in str(a):
        s = s + int(i)
    return s


for i in range(2, 100):
    for j in range(2, 100):
        p = i**j
        s = sum_digit(p)
        if s > maxs:
            maxs = s

print("result = ", maxs)
