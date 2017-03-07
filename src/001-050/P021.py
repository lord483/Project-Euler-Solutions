'''
Amicable numbers
Problem 21
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''


def d(a):
    s = 0
    for i in range(1, a):
        if a % i == 0:
            s = s + i
    return(s)

# test 1
print("220 -", d(220))
print("284 -", d(284))

r = 0

for i in range(2, 10000):
    d1 = d(i)
    if (d1 != i) and (i == d(d1)):
        print(i)
        r = r + i

print("result = ", r)
