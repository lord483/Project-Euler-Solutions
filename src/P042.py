
from math import sqrt

file_name = "p042_words.txt"

f = open(file_name, 'r')
ins = f.read()
ina = list(ins.split(","))
ina = [i[1:-1] for i in ina]

# print(ina)

count = 0
base = ord('A') - 1


def to_num(s):
    r = 0
    for c in s:
        r = r + ord(c) - base
    return r


def is_triangular(n):

    s = int(sqrt(n * 2))
    if n * 2 == s * (s + 1):
        return True
    else:
        return False

for s in ina:
    n = to_num(s)
    if is_triangular(n):
        count += 1

print("result = ", count)
