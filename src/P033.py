def check_nt(a,b):
    # check non triviality , a always < b
    if a > b:
        return False

    #find common digit
    f=0
    c=''

    sa = str(a)
    sb = str(b)

    for i in sa:
        if i in sb:
            f=1
            c=i
            
    if f == 0:
        # Nothing in common
        return False
    
    if c == '0':
        #it's trivial
        #print("It's Trivial")
        return False
        
    na = 0  # new a
    for i in sa:
        if i != c:
            na = int(i)

    nb = 0  # new b
    for i in sb:
        if i != c:
            nb = int(i)
    if (nb == 0 ) or (sb ==0):
        return False
    if (na/nb) == (a/b):
        return True
    else:
        return False

# Test
'''
print(check_nt(49,98))
print(check_nt(43,87))
print(check_nt(30,50)) '''

mi = 1
mj = 1
for i in range(11,100):
    for j in range(i+1,100):
        if check_nt(i,j):
            print(i , j)
            mi = mi * i
            mj = mj*j

print("final",mi , "/",mj)
    
