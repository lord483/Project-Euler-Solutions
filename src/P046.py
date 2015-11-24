'''
Goldbach's other conjecture
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

from math import sqrt

primes =[2,3,5,7]

def is_prime(a):
    l = int(sqrt(a))
    isPrime = True
    for i in primes:
        if i > l:
            break
        elif a%i == 0:
            isPrime = False
            break
    return isPrime


def is_gold(a):
    
    g = False
    
    for i in primes:
        if (i > a-2) or g:
            break
        
        for j in range(1,a):
            n = i+(2*j*j)
            if n > a:
                break
            elif n == a:
                g = True
                break
        
    return g

def main():

    i=7
    gold = True
    while(gold):
        i = i+2
        if is_prime(i):
            primes.append(i)
        else:
            gold = is_gold(i)
            if not gold:
                print(i)
        


if __name__ == "__main__":
    main()
    
