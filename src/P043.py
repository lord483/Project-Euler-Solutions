
def gen_pand(a):
    r=[]
    if a == 1 :
        return ['10']
    else:
        p = gen_pand(a-1)
        c = str(a)
        for s in p:
            for i in range(a+1):
                r.append(s[:i]+c+s[i:])
        print( a , " Len = " , len(r))
        return r

x =[]
x= gen_pand(9)
x2 = []

count = 0
dl = [2,3,5,7,11,13,17]

for s in x:
    f = 0
    for i in range(len(dl)) :
        j = i+1
        n = int(s[j:j+3])
        if n % dl[i] != 0:
            f =1
            break
    if f == 0 :
        x2.append(int(s))
        count += 1

print("count = ", count , " sum =", sum(x2))
        
        
    
                
                
        
