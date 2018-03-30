if __name__ == "__main__":
    a = 3
    b = 2
    n = 1000
    res = 0
    for _ in range(n - 1):
        x = a + 2 * b
        y = a + b
        if len(str(x)) > len(str(y)):
            res += 1

        a, b = x, y

    # print(a,b)
    print(res)
