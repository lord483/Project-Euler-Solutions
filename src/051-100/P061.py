if __name__ == "__main__":
    a, b, c, d, e, f = [], [], [], [], [], []
    for i in range(1, 9999):
        tr = (i * (i + 1)) // 2
        if tr > 9999:
            break
        if (1000 <= tr <= 9999) and (tr % 100 > 9):
            a.append(tr)

        sq = i * i
        if (1000 <= sq <= 9999) and (sq % 100 > 9):
            b.append(sq)

        pe = (i * (3 * i - 1)) // 2
        if (1000 <= pe <= 9999) and (pe % 100 > 9):
            c.append(pe)

        hexa = i * (2 * i - 1)
        if (1000 <= hexa <= 9999) and (hexa % 100 > 9):
            d.append(hexa)

        hepta = i * (5 * i - 3) // 2
        if (1000 <= hepta <= 9999) and (hepta % 100 > 9):
            e.append(hepta)

        octa = i * (3 * i - 2)
        if (1000 <= octa <= 9999) and (octa % 100 > 9):
            f.append(octa)

    print(len(a), len(b), len(c), len(d), len(e), len(f))

    sa = [(i, 3) for i in a] + [(i, 4) for i in b] + [(i, 5) for i in c] \
        + [(i, 6) for i in d] + [(i, 7) for i in e] + [(i, 8) for i in f]

    print(len(sa))
    # u = [k for k, _ in sa]
    # print("len(u): ", len(u))
    # print("len(set(u) : ", len(set(u)))
    # print(len(u) - len(set(u)))

    for i in a:
        l1 = (i % 100) * 100
        l2 = l1 + 100
        f2 = [(k, v) for k, v in sa if (l1 < k < l2) and (v > 3)]
        # print(i,len(f2))
        for k2, v2 in f2:
            l1 = (k2 % 100) * 100
            l2 = l1 + 100
            f3 = [(k, v) for k, v in sa
                  if (l1 < k < l2) and (v not in (3, v2))]
            # print("--",k2,v2,len(f3))
            for k3, v3 in f3:
                l1 = (k3 % 100) * 100
                l2 = l1 + 100
                f4 = [(k, v) for k, v in sa
                      if (l1 < k < l2) and (v not in (3, v2, v3))]
                for k4, v4 in f4:
                    l1 = (k4 % 100) * 100
                    l2 = l1 + 100
                    f5 = [(k, v) for k, v in sa
                          if (l1 < k < l2) and (v not in (3, v2, v3, v4))]
                    for k5, v5 in f5:
                        l1 = (k5 % 100) * 100
                        l2 = l1 + 100
                        f6 = [
                            (k, v) for k, v in sa
                            if (l1 < k < l2) and (v not in (3, v2, v3, v4, v5))
                        ]
                        for k6, v6 in f6:
                            if k6 % 100 == i // 100:
                                print("Result : ", sum([i, k2, k3, k4, k5,
                                                        k6]))
                                print(
                                    "i:{}, k2:{}, v2:{}, k3:{}, v3:{}, k4:{}, v4:{}, k5:{}, v5:{}, k6:{}, v6:{},".
                                    format(i, k2, v2, k3, v3, k4, v4, k5, v5,
                                           k6, v6))
