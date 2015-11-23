'''
Smallest prime factor

Problem 521  

https://projecteuler.net/problem=521 

Let smpf(n) be the smallest prime factor of n.
smpf(91)=7 because 91=7×13 and smpf(45)=3 because 45=3×3×5.
Let S(n) be the sum of smpf(i) for 2 ≤ i ≤ n.
E.g. S(100)=1257.

Find S(10^12) mod 10^9.   
'''

from math import sqrt

LIMIT = 10000000            # The Limit
BASE = 9                    # Number of digits to keep
primes =[2,3]               # array of primes

sumAll = 0                  # the sum of all integers till limit

print("calculating till :" , LIMIT)
#Initialize result

sumAll = ((LIMIT * (LIMIT+1)) >> 1 ) - 1

print("Sum of all integers in the range 2 to ", LIMIT , " is :" , sumAll)

#let's find the primes till SQRT(LIMIT)
l = int(sqrt(LIMIT)) + 1

print("starting to calculate primes till ", l)

s = primes[-1]
for i in range(s+2,l,2):
    isP =  1 
    l2 = sqrt(i)
    for p in primes:
        if p > l2:
            break
        if ((i % p) == 0):
            isP = 0 
            break
    if isP == 1 :
        primes.append(i)

print("# of primes found is ", len(primes), " and the largest is ", primes[-1])

toReduce = 0 

mul = 1
L = len(primes)
for i in range(L):
    p = primes[i]
    mul = mul * p
    if p <=3 : 
        n = int((LIMIT-p)/mul)
        s  = n*(n+1)*mul >> 1
        toReduce = toReduce + s
        print("P = ", p , " n =",n , " s =",s," toReduce=",toReduce)
        
    else:
        #print(p)
        n = int(LIMIT/p)
        for j in range(p, n,2):
            # check if j is prime
            isP = 1 
            for p2 in primes:
                if p2*p2 > j:
                    break
                if j%p2 == 0 :
                    isP = 0
                    break
            if isP== 1:
                s= (j-1)*p
                toReduce += s
                #print(j , s , toReduce)


   

result = sumAll - toReduce
print("Dude your result is ",str(result)[(-1*BASE):])