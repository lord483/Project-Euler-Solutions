'''
Consecutive prime sum
Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from math import sqrt 
primes = [2,3]

def is_prime(a):
    result = True
    l = int(sqrt(a))
    for p in primes:
        if p > l:
            break
        elif a%p == 0:
            result = False
            break
    return result

def main():
    
    for i in range(5,1000000,2):
        if is_prime(i):
            primes.append(i)
            
    #primes_f = [ i for i in primes if i < 1000]
    print("step 1 done : ", len(primes))

    sub = []
    max_s = 0
    max_l =0 
    s = 0
    sl =0
    
    for i in range(len(primes)):
        sub = primes[:i+1]
        s=sum(sub)
        sl =len(sub)
        if s > 1000000:
            break
        if s in primes:
            max_l = sl
            sax_s = s
        else:
            while(sl > max_l):
                sub[:1]=[]
                sl=len(sub)
                s = sum(sub)
                if (s in primes):
                    if sl > max_l:
                        max_l = sl
                        max_s = s
                    
                
            
        
    print(" Done : ", max_s , " len=", max_l)                
                
         

if __name__ == '__main__':
    
    main()
