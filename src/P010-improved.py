def P10(n):
    r = int(n**0.5)
    assert r * r <= n and (r + 1)**2 > n
    V = [n // i for i in range(1, r + 1)]
    print("prior :", V)
    V += list(range(V[-1] - 1, 0, -1))
    print("2nd  :", V)
    #S = {i:i*(i+1)//2-1 for i in V}
    S = [0 for i in range(max(V) + 1)]
    for i in V:
        S[i] = i * (i + 1) // 2 - 1
    print("s : before", S)
    for p in range(2, r + 1):
        print("p = ", p)
        if S[p] > S[p - 1]:  # p is prime
            sp = S[p - 1]  # sum of primes smaller than p
            p2 = p * p
            for v in V:

                if v < p2:
                    break

                print(" v = ", v)
                print("S[v] :", S[v])
                print("v//p :", str(v // p), " S[v//p]:", str(S[v // p]), " sp:", sp)
                S[v] -= p * (S[v // p] - sp)
                print("S[v] after :", S[v])

        print(" S now is ", S)
    print("s : after: ", S)
    return S[n]


print(P10(20))
