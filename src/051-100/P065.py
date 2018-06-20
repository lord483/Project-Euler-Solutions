'''
    Convergents of e
    Problem 65
'''
from fractions import Fraction
u = Fraction(1, 1)
if __name__ == "__main__":
    e = [2, 1, 2, 1]
    for i in range(2, 35):
        e.extend([1, 2 * i, 1])

    e_99 = e[:99]
    res = Fraction(1, e[100])
    for i in e_99[::-1]:
        res = u / res
        res += Fraction(i)

    print(res)
    print("Value of e upto 100 terms is {:.9f}".format(
        res.numerator / res.denominator))
    n = res.numerator
    s = sum(int(c) for c in str(n))
    print("Sum of digits in numerator is : ", s)
