'''
Highly divisible triangular number

Problem 12

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?  '''

a = 7
s = int(a * (a + 1) / 2)
print(" Starting ", a, " ", s)


def find_divisors(x):
    x = int(x)
    n = 1
    i = 1
    while (x > 1) and (i * i <= x):
        i += 1
        c = 0
        while (x % i == 0):
            c = c + 1
            x = x // i

        n *= (c + 1)

    if x > 1:
        n = n * 2

    return n


while (True):
    n1, n2 = 1, 1
    a = a + 1

    if a % 2 == 0:
        n1 = find_divisors(a / 2)
        n2 = find_divisors(a + 1)
    else:
        n1 = find_divisors(a)
        n2 = find_divisors((a + 1) / 2)

    n = n1 * n2

    if (n > 500):
        print("Found ......... ", a, " ", n, " , Triange Number =  ",
              a * (a + 1) / 2)
        break
    if (a % 1000 == 0):
        print(a, " ", n, " , Triange Number =  ", a * (a + 1) / 2)
