def isPall(a):
    if a < 10:
        return True
    s = str(a)
    rs = s[::-1]
    if s == rs:
        return True
    else:
        return False


def toBin(a):
    b = ''
    while (a > 1):
        r = a % 2
        b = str(r) + b
        a = int(a / 2)
    b = str(a) + b
    return(int(b))

'''
a=int(input(" Test Number : "))
while(a!=0):
    print(isPall(a))
    print("Bin = " , toBin(a))
    a=int(input(" Test Number : ")) '''

lim = 1000000
sum_a = 0

for i in range(1000000):
    if isPall(i) and isPall(toBin(i)):
        sum_a = sum_a + i

print('result =', sum_a)
