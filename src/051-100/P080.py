'''
    Problem 80 - Square root digital expansion

    It is well known that if the square root of a natural number is not an integer,
    then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

    The square root of two is 1.41421356237309504880..., and
    the digital sum of the first one hundred decimal digits is 475.

    For the first one hundred natural numbers, find the total of the digital sums of
    the first one hundred decimal digits for all the irrational square roots.
'''

from decimal import *
getcontext().prec = 110

squares  = [i*i for i in range(1,11)]
res = 0
sqrt = Decimal(0.5)
for i in range(1,101):
    if i in squares:
        continue
    d = Decimal(i)**sqrt
    dec,fra = str(d).split(".")
    r = sum([int(c) for c in dec])
    r += sum([int(c) for c in fra[:100-len(dec)]])
    print(i,r)
    res += r

print(res)
