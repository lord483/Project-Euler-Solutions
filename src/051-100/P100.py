'''
    Problem 100 - Arranged probability

    If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs,
    and two discs were taken at random, it can be seen that the probability of taking two blue discs,
        P(BB) = (15/21)×(14/20) = 1/2.

    The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random,
    is a box containing eighty-five blue discs and thirty-five red discs.

    By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total,
    determine the number of blue discs that the box would contain.

    Solved via : https://www.alpertron.com.ar/QUAD.HTM (Diaphantine Equation Solver)
'''

a = 15
b = 6

while (a + b < 10**12):
    a_next = 5 * a + 2 * b - 2
    b_next = 2 * a + b - 1

    a, b = a_next, b_next

print(a, b, a + b)
