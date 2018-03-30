'''
Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
     13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example
having seven primes among the ten generated numbers, yielding the family:
        56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
 '''

from utils import prime

maxi = 999999


def hasThreeRepeating(n):
    '''
    you don't have to check the primes with two or four recurring digits. 
    If you form 8 different numbers with them, at least once the sum of the digits (and the whole number) 
    is divisible by three.
    '''
    numberList = list(str(n))
    numberList.sort()
    s = ""
    for i in numberList:
        s += str(i)

    for c in s:
        if (s.rfind(c) - s.find(c)) == 2:
            return True

    return False


def main():

    primes = prime.getPrimes(maxi)
    print("Step one complete . # = ", len(primes))
    primesFiltered = [i for i in primes if i >= 56000 and hasThreeRepeating(i)]
    print("Step two complete . # = ", len(primesFiltered))
    assert (56333 in primes)
    #assert(56330 in primes)

    intSet = set([i for i in range(0, 10)])

    for p in primesFiltered:
        s = str(p)
        found = False
        intList = set([int(i) for i in s])
        for i in intList:
            foundCount = 1
            pl = []
            for j in intSet:
                if (i != j):
                    newInt = int(s.replace(str(i), str(j)))
                    l = len(str(newInt))
                    if (l > 5) and (newInt in primes):
                        foundCount += 1
                        pl.append(newInt)
                        #print(p," ",newInt)
            if (foundCount >= 7):
                print(s, foundCount, pl)
                if foundCount > 7:
                    found = True
                    break
        if found:
            break


if __name__ == '__main__':
    main()
    print("Progam completed")
