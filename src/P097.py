'''
    Large non-Mersenne prime
    Problem 97

    find last 10 digits of 28433×(2^7830457) + 1.

'''
if __name__ == "__main__":
    p = 7830457
    m = 28433
    mod = 10**10
    r = 1
    for i in range(p):
        r = (r * 2) % mod

    r = (r * m) % mod

    print(r + 1)
