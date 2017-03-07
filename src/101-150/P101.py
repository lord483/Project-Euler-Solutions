def eval_t(p, n):
    res = 0
    for i in range(len(p)):
        t = p[i] * (n**i)
        res = res + t
    return res


def eval_p(p, n):
    res = []
    for i in range(n + 1):
        res.append(eval_t(p, i))
    return res

#op = [(-1)**(i+2) for i in range(10) ]
p3 = [0, 0, 0, 1]
op = p3
ol = eval_p(op, 10)
print("Original polynomial: ", op, " - original values: ", ol)


def find_fit(s):
    l = len(s)
    p = [1 for i in range(l)]
