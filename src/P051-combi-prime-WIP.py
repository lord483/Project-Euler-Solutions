'''
Prime digit replacements
Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
     13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example 
having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
 '''

from math import sqrt

maxi = 999999
primes=[2,3,5,7]

def set_prime():
    for i in range(9,maxi,2):
        b = int(sqrt(i))+1
        for p in primes:
            if i%p == 0:
                break
            if p > b:
                primes.append(i)
                break
    
        
def main(): 

    set_prime()
    print("Step one complete . # = ", len(primes))

    primes[:4] = []
    # main logic
    for p in primes:
        pass

if __name__ == '__main__':
    main()

    
