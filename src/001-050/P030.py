'''
Digit fifth powers
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.  '''


def sum_digit(a):
    s = 0
    for c in str(a):
        i = int(c)
        s = s + pow(i, 5)
    return s


res = 0
num_list = []

for i in range(10, 999999):
    if i == sum_digit(i):
        num_list.append(i)

print(sum(num_list))
print("list of numbers = ", num_list)
