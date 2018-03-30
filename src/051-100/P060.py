from utils import prime
from time import time
from functools import lru_cache

lim = 10**7
start = ['3', '7', '109', '673']


@lru_cache(maxsize=2000000)
def check_prime(x):
    y = int(x**0.5) + 1

    for j in primes:
        if j > y:
            return True
        if x % j == 0:
            return False

    return True


def isPrime(x):
    x = int(x)

    if x in pset:
        return True
    if x < lim:
        return False
    else:
        return check_prime(x)


def checkList(X, y):
    for xi in X:
        if not isPrime(xi + y):
            return False
        if not isPrime(y + xi):
            return False
    return True


if __name__ == "__main__":
    t0 = time()

    primes = prime.getPrimes(lim)
    pset = set(primes)
    t1 = time()
    print("Number of primes = {:,}".format(len(primes)))
    print("Time taken = {:.2f} secs".format(t1 - t0))

    res = 0

    # let's find all three pair

    n = 1500
    pk = primes[1:n + 1]
    results = []
    for i in range(len(pk)):
        print(i, pk[i])
        si = str(pk[i])
        for j in range(i + 1, len(pk)):
            sj = str(pk[j])
            if isPrime(si + sj) and isPrime(sj + si):
                for k in range(j + 1, len(pk)):
                    sk = str(pk[k])
                    if checkList([si, sj], sk):
                        for l in range(k + 1, len(pk)):
                            sl = str(pk[l])
                            if checkList([si, sj, sk], sl):
                                for m in range(l + 1, len(pk)):
                                    sm = str(pk[m])
                                    if checkList([si, sj, sk, sl], sm):
                                        print("found : ", si, sj, sk, sl, sm)
                                        r = pk[i] + pk[j] + pk[k] + pk[l] + pk[m]
                                        print(" Result = ", r)
                                        results.append(r)

    print("Number of 5-lets = ", len(results))
    # print(results)
    print("Final result =")
    print(min(results))
