'''
Pandigital products
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.  '''


def is_pand(a):
    s = str(a)
    l = len(s)
    if l == 1:
        return True
    if '0' in s:
        return False

    for i in range(0, l):
        if (s[i] in s[i + 1:]) and (s[i] != ' '):
            return False
    return True

# Test
'''
a=int(input("num = "))
while(a != 0):
    print(is_pand(a))
    a=int(input("num = ")) '''

num_list = []

for i in range(2, 100000):
    if is_pand(i):
        for j in range(2, 100000):
            p = i * j
            l1 = len(str(i))
            l2 = len(str(j))
            l3 = len(str(p))
            l = l1 + l2 + l3
            if l > 9:
                break
            if l == 9:
                if is_pand(str(i) + str(j) + str(p)):
                    if p not in num_list:
                        num_list.append(p)

print("Total nums =", len(num_list))
print("list: ", num_list)
print("sum = ", sum(num_list))
