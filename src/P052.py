'''
Permuted multiples
Problem 52
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

i = 0
f = True
while(f):
    i = i + 1
    p1 = [c for c in str(i)]

    if p1[0] == '1':
        p2 = [c for c in str(i * 2)]
        p1.sort()
        p2.sort()
        if p1 == p2:
            p3 = [c for c in str(i * 3)]
            p3.sort()
            if p2 == p3:
                p4 = [c for c in str(i * 4)]
                p4.sort()
                if p3 == p4:
                    p5 = [c for c in str(i * 5)]
                    p5.sort()
                    if p4 == p5:
                        p6 = [c for c in str(i * 6)]
                        p6.sort()
                        if p5 == p6:
                            print(i)
                            f = False
