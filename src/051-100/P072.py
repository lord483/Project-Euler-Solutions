'''
    Problem 72 - Counting fractions

    Consider the fraction, n/d, where n and d are positive integers.
    If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

    If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

        1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

        It can be seen that there are 21 elements in this set.

    How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000 ?

'''
'''
    Solution : It can be seen that the solution is:
        sum(phi(i)) for i in range(2, 1000001)

    We can use Euler's formula and a seive to compute it easily

'''
N = 10**6
# import numpy as np
# arr = np.arange(N+1)
# print(arr.shape)

arr = [i for i in range(N + 1)]
result = 0
for i in range(2, N + 1):
    if arr[i] == i:
        for j in range(i, N + 1, i):
            arr[j] = (arr[j] // i) * (i - 1)
    result += arr[i]

print(result)
