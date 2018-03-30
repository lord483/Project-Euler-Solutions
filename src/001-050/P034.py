'''
Digit factorials
Problem 34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included. '''

fact = [1, 1]
for i in range(2, 10):
    fact.append(fact[-1] * i)

print(fact)

n = 10
ms = 0

l = 0
while (True):
    l = l + 1
    if fact[9] * l < pow(10, l):
        break
print("l=", l)
for n in range(10, pow(10, l) - 1):
    n = n + 1
    s = 0
    for c in str(n):
        s = s + fact[int(c)]
    if s == n:
        ms = ms + s
        print(n)
        # break

print("Result = ", ms)
