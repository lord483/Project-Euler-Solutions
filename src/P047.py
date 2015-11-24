'''
Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''

from math import sqrt

primes =[2,3]
facts=[0,1,1,1]

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


def num_facts(a):
    n = 0
    i = -1
    l = int(sqrt(a))
    while(a>1):
        i=i+1
        p=primes[i]
        if p > l:
            n = n +1
            a = 1
        elif a%p ==0:
            n=n+1
            while(a%p == 0):
                a = a //p
    return n


def main():
    i=3
    four = False
    while(not four):
        i = i+1
        p=0
        if i%2 ==1:
            if is_prime(i):
                primes.append(i)
                facts.append(1)
                p=1
                
        if p==0:        
            facts.append(num_facts(i))

        if facts[-1] == 4:
            if facts[-2] == 4:
                if facts[-3] == 4:
                    if facts[-4] == 4:
                        four = True
                        print("found !!! ", i)
        
        facts[:1]=[]
        '''
        if i%10000 == 1:
            l  = len(facts)
            print("now : " , i , "   ", len(facts))  '''
            
if __name__ == "__main__":
    main()
    
