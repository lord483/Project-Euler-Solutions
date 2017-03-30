from time import time
import numpy as np

MAX = 10**6


def find_div_sum(n):
    a = np.ones(n + 1)
    lim = int(n**0.5)
    for i in range(2, n // 2 + 1):
        a[i * 2:n + 1:i] += i

    a[a > MAX] = 0

    return a


def find_chains(div_sum):
    l, n = 0, 0

    for i in range(10, MAX + 1):
        cl = 1
        next_num = int(div_sum[i])
        visited = [i]
        while True:
            if next_num <= 1:
                cl = 0
                break
            elif next_num in visited:
                if next_num != i:
                    cl = 0
                break

            visited.append(next_num)
            next_num = int(div_sum[next_num])
            cl += 1

        if cl > l:
            l = cl
            n = min(visited)

    return l, n


if __name__ == "__main__":
    t0 = time()
    div_sum = find_div_sum(MAX)
    div_sum.astype(int)
    l, n = find_chains(div_sum)
    print(l, n)
    print("Time takenn = {:.2f} sec".format(time() - t0))
