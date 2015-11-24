'''
Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that,
the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

ab=[]
sum_list=[]
res = 0

from math import sqrt

def abundant(a):
    
    s = 1
    lim=int(sqrt(a))+1
        
    for i in range(2,lim):
        if a%i == 0:
            b = int(a/i)
            if b != i :
                s = s + i + b
            else:
                s = s + i
        if s > a:
            break
                
    if s > a:
        return True
    else:
        return False

#limit = 8000
limit = 28124

for i in range(1,limit):
    if abundant(i):
        ab.append(i)

    nab = 0
    for j in ab:
        if j>(i/2):
            break
        if i-j in ab:
            nab = 1
            break
        
    if nab ==0:
        res=res+i
        
    if i%1000 == 0:
        print("i =",i , " , Res=",res)

print("Total ab found = ", len(ab)," first = ",ab[0],"  last = ",ab[-1])


'''
for i in range(1,limit):
    nab = 0
    for j in ab:
        if j>i:
            break
        if i-j in ab:
            nab = 1
            break
        
    if nab ==0:
        res=res+i
        
    if i%1000 == 0:
        print("i =",i , " , Res=",res)
        '''
        
print("result =" , res)

        



