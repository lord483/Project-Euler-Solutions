'''
Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?  '''

from math import sqrt

LIMIT = 1000000
primes=[2,3,5,7]
loop = 0
sl=0

for i in range(9,LIMIT,2):
    loop = loop +1
    l = int(sqrt(i))+1
    for p in primes:
        sl=sl+1
        if i%p == 0:
            break
        if p >l:
            primes.append(i)
            break

#print("Loop =", loop , " ",sl)       
#print(primes)
print("all Primes computed , count = " ,len(primes))

'''
def permutation_list(p):
    li = []
    dl =[]
    for c in str(p):
        dl.append(int(c))
    

    
# find those weird sets
for p in prime:
    pl = permutation_list(p)  '''
    
    
    


