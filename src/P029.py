a = 100
b = 100

num_list = []

for i in range(2, a + 1):
    for j in range(2, b + 1):
        p = pow(i, j)
        if p not in num_list:
            num_list.append(p)

print(len(num_list))
