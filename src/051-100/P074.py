'''
    Problem 74 - Digit factorial chains
'''


def solve(N):
    factorial = [1]
    for i in range(1, 10):
        factorial.append(factorial[-1] * i)

    res = 0

    for n in range(3, N):
        fc = set([n])  # Factorial chain
        cnt = 1
        m = n
        while(True):
            s = sum((factorial[int(c)] for c in str(m)))
            if s in fc:
                break
            fc.add(s)
            m = s
            cnt += 1
            if cnt > 60:
                break

        if cnt == 60:
            res += 1

    return res

if __name__ == "__main__":
    from time import time
    t0 = time()
    print(solve(10**6))
    print("done in {:.2f} sec".format(time() - t0))
