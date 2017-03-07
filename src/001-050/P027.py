'''
Quadratic primes
Problem 27

Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.  '''

from math import sqrt


def is_prime(a):
    if a < 0:
        return False
    lim = int(sqrt(a)) + 1
    for i in range(2, lim):
        if a % i == 0:
            return False
    return True

c = 41
b = 1
a = 1


def eval_quad(a, b, c, x):
    return a * x * x + b * x + c

'''
for i in range(0,50):
    e = eval_quad(a,b,c,i)
    print( i , e , is_prime(e))  '''

max_seq = 0
max_set = []
for b in range(-999, 999):
    for c in range(-999, 999):
        n = 0
        while(is_prime(eval_quad(a, b, c, n))):
            n = n + 1
        if n > max_seq:
            max_seq = n
            max_set = [a, b, c]

print(max_seq, max_set)
result = max_set[1] * max_set[2]
print(result)
