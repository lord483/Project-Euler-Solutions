from sympy import binomial

if __name__ == "__main__":
    n = 100

    res = 1
    for i in range(2,n):
        r = binomial(n-1,i-1)/i
        res += r

    print(res)
