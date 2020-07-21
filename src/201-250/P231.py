
import numpy as np


def get_primes(n):
    arr = np.ones(n + 1, dtype=np.int8)
    arr[0], arr[1] = 0, 0
    for i in range(2, n + 1):
        if arr[i]:
            arr[i * i:n + 1:i] = 0
    return arr.nonzero()[0]


def count_of_occurrences(n, p):
    """
    Return Number of times 'p' occurs in  n! 

    for eg: f(30 , 7) = 4
    """
    cnt = 0
    while n:
        n //= p
        cnt += n
    return cnt


def p231(n, r):
    primes = get_primes(n)

    res = 0

    for p in primes:
        res += p*(count_of_occurrences(n, p) -
                  count_of_occurrences(r, p) - count_of_occurrences(n-r, p))

    return res

if __name__ == "__main__":
    print(p231(20000000,5000000))
