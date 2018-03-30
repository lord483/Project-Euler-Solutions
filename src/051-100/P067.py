f = open("P067_triangle.txt", 'r')
s = 0
lines = 0
p = []

for l in f:
    p.append(list(map(int, l.split())))

p2 = []
p2.append(p[0])

for i in range(1, len(p)):
    n = p[i]
    m = []
    l = len(n)

    for j in range(0, l):

        pmax = 0
        if j == 0:
            pmax = p2[i - 1][0]
        elif j == l - 1:
            pmax = p2[i - 1][-1]
        elif p2[i - 1][j - 1] > p2[i - 1][j]:
            pmax = p2[i - 1][j - 1]
        else:
            pmax = p2[i - 1][j]

        m.append(n[j] + pmax)

    p2.append(m)

# print(" Weights")
# for l in p2:
#     print(l)
# print(" ===== ")
# # print(p2[-1])
p2[-1].sort()

print(" Result =", p2[-1][-1])
