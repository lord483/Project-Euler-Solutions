# -*- coding: cp1252 -*-

'''
Problem 15

Lattice paths


Starting in the top left corner of a 2�2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20�20 grid?
'''


def solve(SIZE):
    r = [[0 for i in range(SIZE + 1)] for j in range(SIZE + 1)]

    for i in range(SIZE + 1):
        for j in range(SIZE + 1):
            if i == SIZE or j == SIZE:
                r[i][j] = 1

    r[SIZE][SIZE] = 0

    for i in range(SIZE - 1, -1, -1):
        for j in range(SIZE - 1, -1, -1):
            r[i][j] = r[i][j + 1] + r[i + 1][j]

    return(r[0][0])

if __name__ == "__main__":
    SIZE = int(input("Enter the size : "))
    print(" Answer =", solve(SIZE))
