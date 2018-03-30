'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number? '''

from math import sqrt


def isPrime(a):
    l = int(sqrt(a))
    for p in primes:
        if p > l:
            return True
        elif a % p == 0:
            return False

    return True


'''
a=input("Enter a num :")
print isPrime(a)
'''

primes = [2, 3]
s = 3

while len(primes) < 10001:
    s = s + 2
    if isPrime(s):
        primes.append(s)
        if len(primes) % 500 == 0:
            print(len(primes), " ", s)

print(len(primes), "  ", primes[-1])
