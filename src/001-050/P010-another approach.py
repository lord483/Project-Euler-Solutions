'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from math import sqrt


def isPrime(a):
    for i in p:
        if a % i == 0:
            return False
            break

    return True

'''
a=input("Enter a num :")
print isPrime(a)
'''

p = [2, 3]
s = 3
sum = 5

while s < 2000000:
    s = s + 2
    if isPrime(s):
        p.append(s)
        sum = sum + s
    if s % 100000 == 1:
        print s

print "Result = ", sum
