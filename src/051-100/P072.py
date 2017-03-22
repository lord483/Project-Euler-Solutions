
n = 8
res = n-1

for i in range(2,n):
    m = (n-i)//i
    res += (n-i-m)
print(res)
