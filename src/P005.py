def gcf(a, b):
    if a < b:
        a, b = b, a
    elif a == b:
        return a

    r = a % b
    gcf = b

    while r != 0:
        a, b = b, r
        r = a % b
        gcf = b

    return gcf

'''
a=input("first number  : ")
b=input("second number : ")

print "GCF = ", gcf(a,b)
'''

ra = int(input(" Enter Range : "))
mul = 1
for i in range(1, ra + 1):
    if mul % i != 0:
        r = i / gcf(mul, i)
        mul = mul * r
    print(i, " ", mul)

print(" O/P :", mul)
