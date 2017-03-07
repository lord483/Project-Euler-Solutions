
penta = []
max_l = 10001


def penta_num(n):
    p = (3 * n - 1) * n / 2
    p = int(p)
    return p

penta = list(map(penta_num, range(1, max_l)))

pmax = penta[-1]
print(" First step complete : ", pmax)
print(penta[:20])


for i in range(max_l - 1):
    pi = penta[i]
    f = 0
    for j in range(i):
        pj = penta[j]
        d = pi - pj

        if (d in penta):
            s = pi + pj
            print("temp found : ", i + 1, ' ', pi, ' ', j + 1, ' ', pj, ' ', d, " ", s)
            if s in penta:
                print("found : ", i + 1, ' ', pi, ' ', j + 1, ' ', pj, ' ', d, " ", s)
                f = 1
                break
    if i % 500 == 0:
        print("Now at : ", i)
    if f == 1:
        break
'''
'''
