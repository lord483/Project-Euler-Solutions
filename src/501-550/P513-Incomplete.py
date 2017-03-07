'''
Problem 513  - Integral median

	ABC is an integral sided triangle with sides a≤b≤c.
	mc is the median connecting C and the midpoint of AB. 
	F(n) is the number of such triangles with c≤n for which mc has integral length as well.
	F(10)=3 and F(50)=165.

	Find F(100000). '''

from math import sqrt

n = 50

if __name__ == "__main__":
    res = 0
    for c in range(2, n + 1, 2):
        c2 = c * c
        for a in range(1, c):
            a2 = 2 * (a * a)
            r = max(c - a + 1, a)
            for b in range(r, c + 1):
                # now check for int median
                s = a2 + (2 * b * b) - c2
                m = sqrt(s) / 2
                if m == int(m):
                    print(a, b, c, m)
                    res = res + 1
    print(res)
