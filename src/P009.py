def main_process(n):
    res = -1
    m = (n//2)+1
    for a in range(2,m):
        mb = ((n-a) // 2 ) + 1
        for b in range(a+1,mb):
            c = n - (a+b)
            #print('eval ',a,b,c)
            if c*c == (a*a + b*b):
                print(a,b,c)
                mul = a*b*c
                if (mul > 0) and (mul > res) :
                    res = mul
    return res         
    
if __name__ == '__main__':
    t = int(input())
    for ti in range(t):
        n = int(input())
        res = main_process(n)
        print(res)
