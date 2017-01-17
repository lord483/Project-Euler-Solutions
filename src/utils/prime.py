# A function to find out all the primes till the number n
#
# @Author : Subhendu Ranjan Mishra <subhendu_mishra@infosys.com>
#
# @Input : a positive intiger
# @Output : An array of intigers

from itertools import *
from array import array
from time import time


def getPrimes(n):
    r = n // 2
    # plist = list(islice(repeat(1), r + 1))
    plist = array("I", islice(repeat(1), r + 1))
    plist[0] = 0

    lim = int((n**0.5) / 2 + 1)

    for i in range(1, lim + 1):
        p = 2 * i + 1

        if plist[i]:
            sp = 2 * i * (i + 1)
            while(sp <= r):
                plist[sp] = 0
                sp = sp + p

    primes = array("l", [2] + [(2 * i + 1) for i in range(r) if plist[i]])
    return primes


def getPrimes2(n):
    r = n
    # plist = list(islice(repeat(1), r + 1))
    plist = array("I", islice(repeat(1), r + 1))
    plist[0] = 0
    plist[1] = 0

    lim = int(n**0.5)

    for i in range(2, lim + 1):
        p = i
        if plist[i]:
            sp = i * i
            while(sp <= r):
                plist[sp] = 0
                sp = sp + p

    primes = array("l", (i for i in range(r) if plist[i]))
    return primes

if __name__ == '__main__':
    n = int(input("Enter a number : "))
    t0 = time()
    primes = getPrimes(n)
    print("done : ", len(primes))
    print("Time Taken : {:.2f} seconds".format(time() - t0))
