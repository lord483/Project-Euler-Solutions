'''Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms. '''

f1 = 1
f2 = 2
sum_even = 0

LIMIT = 4000000

while f2 < LIMIT:
    if f2 % 2 == 0:
        sum_even += f2
    new = f1 + f2
    f1 = f2
    f2 = new

print(sum_even)
