'''
    Square digit chains
    Problem 92 : https://projecteuler.net/problem=92
    
    A number chain is created by continuously adding the square of the digits in
    a number to form a new number until it has been seen before.

    For example,

    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

    Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
    What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

    How many starting numbers below ten million will arrive at 89?
'''

from time import time


def check(n):
    if mem[n] > 0:
        return mem[n]
    m = sum([int(c)**2 for c in str(n)])
    r = check(m)
    mem[n] = r
    return r

if __name__ == "__main__":
    t0 = time()
    lim = 81 * 7
    mem = [0 for i in range(lim + 1)]
    mem[1] = 1
    mem[89] = 89

    cnt = 0
    for i in range(1, lim + 1):
        if check(i) == 89:
            cnt += 1

    for i in range(lim + 1, 10**7):
        m = sum([int(c)**2 for c in str(i)])
        if mem[m] == 89:
            cnt += 1
        if i % (10**6) == 0:
            print(i, "  ", cnt)

    print("Result = ", cnt)
    print("Time taken : {:.2f} sec".format(time() - t0))
