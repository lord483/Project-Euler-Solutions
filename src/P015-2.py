# -*- coding: cp1252 -*-

'''
Problem 15

Lattice paths


Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''

r = []
for i in range(0, 21):
    s = []
    for j in range(0, 21):
        if i == 20 or j == 20:
            s.append(1)
        else:
            s.append(0)
    r.append(s)

r[20][20] = 0
print("Start ")
for line in r:
    print(line)

for i in range(19, -1, -1):
    for j in range(19, -1, -1):
        r[i][j] = r[i][j + 1] + r[i + 1][j]

print("end ")
for line in r:
    print(line)
print(" final result  =", r[0][0])
