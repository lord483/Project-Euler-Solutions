'''

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''


def isPalindrome(a):

    digits = []

    if a < 0:
        num = a * -1
    else:
        num = a

    if num >= 0 and num <= 9:
        return True

    while num > 0:
        r = num % 10
        digits.append(r)
        num = int((num - r) / 10)

    #print(a, " digits : " , digits, " . length :" , len(digits))

    p = 1

    for i in range(1, len(digits)):
        if digits[i - 1] != digits[i * -1]:
            p = 0
            break

    if p == 0:
        return False
    else:
        return True


'''
print(33,isPalindrome(33))
a=343
print(a,isPalindrome(a))
a=544
print(a,isPalindrome(a))
a=9090
print(a,isPalindrome(a))
a=9009
print(a,isPalindrome(a)) '''

# Main Logic

p = [0]
for i in range(101, 1000):
    for j in range(100, i):
        a = i * j
        if isPalindrome(a):
            if p[0] < a:
                p.insert(0, a)
            else:
                p.append(a)


print(p)
