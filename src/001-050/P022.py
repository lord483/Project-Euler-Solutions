d = {}
cset = 'abcdefghijklmnopqrstuvwxyz'
n = 0
for i in cset:
    n = n + 1
    d[i] = n
# print(d)

f = open("p022_names.txt", 'r')
r = []
ip = f.read().split(",")
f.close()
# print("Input=",ip)

for i in ip:
    s = i.lower()[1:-1]
    p = 0
    for j in range(0, len(r)):
        if s > r[j]:
            p = j + 1
        else:
            break
    r.insert(p, s)

# f.close()

f2 = open("p022_names_sorted.txt", 'w')

f2.writelines('\n'.join(r))

f2.close()
print(" sorting complete")

rank = 0
res = 0

for name in r:
    rank = rank + 1
    ds = 0
    for c in name:
        ds = ds + d[c]

    res = res + (rank * ds)

print("Final result = ", res)
