# A function to find out all the primes till the number n
#
# @Author : Subhendu Ranjan Mishra <subhendu_mishra@infosys.com>
#
# @Input : a positive intiger
# @Output : An array of intigers

from itertools import *


def getPrimes(n):
    r = n // 2
    plist = list(islice(repeat(True), r + 1))
    plist[0] = False

    lim = int((n**0.5) / 2 + 1)

    for i in range(1, lim + 1):
        p = 2 * i + 1

        if plist[i]:
            sp = 2 * i * (i + 1)
            while(sp <= r):
                plist[sp] = False
                sp = sp + p

    primes = [2] + [(2 * i + 1) for i in range(r) if plist[i]]
    return primes


if __name__ == '__main__':
    n = int(input("Enter a number : "))
    primes = getPrimes(n)
    print("done : ", len(primes))
