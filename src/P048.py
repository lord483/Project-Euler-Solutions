'''
Self powers
Problem 48
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

s =0
lim = 10000000000

for i in range(1,1001):
    '''
    p = 1
    for j in range(1,i+1):
        p=p*i
        if p > lim:
            p = p%lim   '''
    
    pw = i ** i
    p = int(str(pw)[-10:])  
    s = s+p 
    if s > lim:
        s=s%lim

print("result = " , s)
            
