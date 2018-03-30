'''
                75
              95 64
             17 47 82
            18 35 87 10
           20 04 82 47 65
          19 01 23 75 03 34
         88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
       41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

f = open("P018.txt", 'r')
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
# print(p2[-1])
p2[-1].sort()

print(" Result =", p2[-1][-1])
