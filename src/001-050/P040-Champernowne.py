s = ''
i = 1
while(True):
    s = s + str(i)
    i = i + 1
    if len(s) > 1000000:
        break


print(i)

r = 1
r = r * int(s[1 - 1])
r = r * int(s[10 - 1])
r = r * int(s[100 - 1])
r = r * int(s[1000 - 1])
r = r * int(s[10000 - 1])
r = r * int(s[100000 - 1])
r = r * int(s[1000000 - 1])

print("result = ", r)
