'''
Problem 37-Truncatable primes

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.  '''

from math import sqrt

primes = [2]
primes_s = ['2']
sp = []  # Selected Primes
i = 1
limit = 0


def check_sp(s):
    # s=str(a)
    l = len(s)
    for i in range(l):
        if s[i:] not in primes_s:
            return False
        l1 = l - i
        if s[:l1] not in primes_s:
            return False

    return True


def is_prime(a):
    b = int(sqrt(a)) + 1
    for p in primes:
        if a % p == 0:
            return False
            break
        if p > b:
            return True
    return True

while(limit < 11):

    i = i + 2

    if is_prime(i):
        primes.append(i)
        s = str(i)
        primes_s.append(s)

        f = True
        for c in s:
            if c in ['0', '4', '6', '8']:
                f = False
                break

        if i > 10 and f:
            if check_sp(s):
                sp.append(i)
                limit = limit + 1
                print("#", limit, " - ", i, "Number of primes found : ", len(primes))


print("Number of primes found : ", len(primes))
# print(primes)
print("# of specials:", len(sp))
print(sp)
print("Final : ", sum(sp))
