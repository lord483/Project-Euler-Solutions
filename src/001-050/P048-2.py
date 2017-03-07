'''
Self power  -  Problem 48    (An Alternate approach)

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

n = 1000
s = 0
step = 20

for i in range(1, n + 1):
    p = 1
    if i % 10 == 0:
        p = 0
    elif i > step:
        stub = i**step
        stub = int(str(stub)[-10:])
        for j in range(step, i + 1, step):
            p = p * stub
            p = int(str(p)[-10:])
        r = i % step
        pr = i**r
        pr = int(str(pr)[-10:])
        p = p * pr
    else:
        p = i**i

    s = s + p
    s = int(str(s)[-10:])


print(s)
