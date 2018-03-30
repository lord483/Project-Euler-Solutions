''''
Problem 39-Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?    '''

maxs = 0
maxn = 0
'''
If both a and b are even, c will also be even and P (the perimeter) will be even.
If both a and b are odd, c will be even and P will be even.
If one is even and the other is odd, c will be odd and P will again be even.
Therefore, only even values of P need to be checked.  '''

for i in range(6, 1001, 2):
    l = int(i / 3)
    s = 0
    for a in range(2, l):
        l2 = i - a - l - 1
        l3 = int(i / 2)
        lb = min(l2, l3)
        for b in range(a + 1, lb):
            c = i - (a + b)
            if (a * a + b * b) == c * c:
                s = s + 1
    if s > maxs:
        maxs = s
        maxn = i
        print(i, " ", s)
