'''
Prime permutations
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
    is unusual in two ways:
        (i) each of the three terms are prime, and,
        (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from math import sqrt
primes = [2, 3]


def is_prime(a):
    result = True
    l = int(sqrt(a))
    for p in primes:
        if p > l:
            break
        elif a % p == 0:
            result = False
            break
    return result


def main():

    for i in range(5, 10000, 2):
        if is_prime(i):
            primes.append(i)

    primes_f = [i for i in primes if i > 1000]
    print("step 1 done : ", len(primes), " ", len(primes_f))

    for p1 in primes_f:
        p2 = p1 + 3330
        p3 = p2 + 3330

        if p2 > 9999 or p3 > 9999:
            pass
        elif (p2 in primes_f) and (p3 in primes_f):
            p1_list = [c for c in str(p1)]
            p2_list = [c for c in str(p2)]
            p3_list = [c for c in str(p3)]

            p1_list.sort()
            p2_list.sort()
            p3_list.sort()

            if (p1_list == p2_list) and (p2_list == p3_list):
                print(p1, p2, p3)

if __name__ == '__main__':

    main()
