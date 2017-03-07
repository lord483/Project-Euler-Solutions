from math import sqrt

primes = [2]
sp = [2]  # Selected Primes

limit = 1000000


def check_sp(a):
    if a < 10:
        return True
    for c in str(a):
        if c in ['0', '2', '4', '5', '6', '8']:
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

for i in range(3, limit, 2):
    if is_prime(i):
        primes.append(i)
        if check_sp(i):
            sp.append(i)


print("Number of primes found : ", len(primes))
# print(primes)
print("# of specials:", len(sp))
# print(sp)


# Check rotation

spp = []
#r = []


def rotation(a):
    r = []
    if a < 10:
        return r
    s = str(a)
    p = s
    for i in range(len(s)):
        n = p[-1] + p[:-1]
        p = n
        r.append(int(n))
    return r

#print("test: ", rotation(197))


for p in sp:
    f = 0
    # r=[]
    for i in rotation(p):
        if i not in sp:
            f = 1
            break
    if f == 0:
        spp.append(p)

print("total circular prime = ", len(spp))
# print(spp)

# input()
