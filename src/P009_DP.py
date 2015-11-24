pytho=[]
from math import sqrt
def init_pytho(n):
    for i in range(n+1):
        pytho.append(-1)
    return
        
def get_pytho(n):
    m = (n//2)+1
    for a in range(2,m):
        mb = ((n-a) // 2 ) + 2
        for b in range(a+1,mb):
            if a+b >= m:
                break
            else:
                c = sqrt(a*a + b*b)
                s= int(a+b+c)
                if c == int(c)  and s <= n:
                    mul = a*b*c
                    if pytho[s] < mul:
                        pytho[s] = int(mul)
    return

if __name__ == '__main__':
    #t = int(input())
    N = 30
    init_pytho(N)

    print(pytho)
    
    get_pytho(N)

    print(pytho)
