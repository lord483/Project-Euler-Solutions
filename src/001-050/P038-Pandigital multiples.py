'''
Pandigital multiples
Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1? '''

maxp = 0


def is_pand(s):
    # s=str(a)
    if len(s) == 1:
        return True
    if '0' in s:
        return False
    for i in range(len(s) - 1):
        if s[i] in s[i + 1:]:
            return False

    return True


'''
s=input("Enter  Number : ")
a=int(s)

while(a!=0):
    print(is_pand(s))
    s=input("Enter  Number : ")
    a=int(s)  '''

for i in range(9999):
    s = str(i)
    f = is_pand(s)
    j = 1
    while (f):
        if len(s) == 9:
            print(i, " ", j, " ", s)
            maxp = max(maxp, int(s))
            break
        j = j + 1
        n = i * j
        s = s + str(n)
        f = is_pand(s)

print("Result = ", maxp)
