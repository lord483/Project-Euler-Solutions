'''
    Almost equilateral triangles
    Problem 94
'''
from numba import jit


@jit
def is_area_int(L):
    lim = (L // 3) + 1
    sol = 0
    for a in range(3, lim, 2):
        for i in (-1, 1):
            b = a + i
            p = a + a + b
            b_h = b // 2
            hsqrd = a * a - b_h * b_h
            h = int(hsqrd**0.5)
            if h * h == hsqrd:
                area = h * b
                if area % 2 == 0:
                    if p < L:
                        sol += p
    return sol


if __name__ == "__main__":
    from time import time
    t0 = time()

    L = 10**9
    print("Final Result is :", is_area_int(L))

    print("Time Taken : {:.2f} secs".format(time() - t0))
