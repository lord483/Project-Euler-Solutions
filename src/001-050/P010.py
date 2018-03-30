from math import sqrt

primes = [2, 3, 5]


def isPrime(a):
    limit = int(sqrt(a)) + 1
    for p in primes:
        if p > limit:
            break
        if a % p == 0:
            return False
            break

    return True


def get_primes(n):
    if n <= primes[-1]:
        return
    for i in range(primes[-1] + 2, n + 1, 2):
        if isPrime(i):
            primes.append(i)
    return


if __name__ == "__main__":
    t = int(input())
    for ti in range(t):
        n = int(input())
        pos = get_primes(n)
        res = sum([p for p in primes if p <= n])
        print(len(primes))
        print(res)
