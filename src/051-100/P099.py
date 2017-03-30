import math
input_file = "p099_base_exp.txt"

ip, i = [], 0
with open(input_file) as f:
    for line in f:
        i += 1
        a, b = map(int, line.strip().split(","))
        ip.append((i, b * math.log(a)))

ip.sort(key=lambda x: x[1])

print(ip[-1][0])
