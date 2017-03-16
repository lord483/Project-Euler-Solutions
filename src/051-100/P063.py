res = 0
for i  in range(1,26):
    for j in range(1,10):
        if len(str(j**i)) == i:
            res += 1

print(res)
