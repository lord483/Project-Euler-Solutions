'''
Pandigital prime
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists? '''

from math import sqrt

maxp = 0
primes = [2, 3, 5, 7]


def gen_all(a):
    p = []

    if a == 2:
        return ['12', '21']
    s = str(a)
    pp = gen_all(a - 1)
    for i in pp:
        for j in range(a):
            pi = i[:j] + s + i[j:]
            p.append(pi)
    return p


def gen_pand_pc(a):
    p = []
    if a > 9:
        return p
    n = int(a * (a + 1) / 2)
    if n % 3 == 0:
        return p
    s = str(a)
    #li = list(range(a,0,-1))
    pp = gen_all(a - 1)
    for i in pp:
        for j in range(a):
            pi = i[:j] + s + i[j:]
            if pi[-1] not in ['2', '4', '5', '6', '8']:
                p.append(int(pi))
    return p


def is_prime(a):
    b = int(sqrt(a)) + 1
    for p in primes:
        if a % p == 0:
            return False
            break
        if p > b:
            return True
    return True


maxi = 7654321
lim = int(sqrt(maxi)) + 1

for i in range(9, lim, 2):
    if is_prime(i):
        primes.append(i)

print("Step one complete . # = ", len(primes))

p = gen_pand_pc(7)
print("all comb for 7 generated , # =", len(p))

for i in p:
    ii = int(i)
    if is_prime(ii):
        maxp = max(ii, maxp)
        # print(ii)
print("Final = ", maxp)

# print(gen_all(3))
