import numpy as np
from time import time
from numba import jit


# @jit
def solve(times):
    upper = 2**32 - 1
    cnts = 0
    m = 0
    for _ in range(times):
        cnt = 0
        r = 0
        random_block = np.random.randint(
            low=0, high=upper, size=40, dtype="uint32")
        while (r != upper):
            r = r | random_block[cnt]
            cnt += 1

        m = cnt if cnt > m else m
        cnts += cnt

    print("Max : ", m, " steps: ", times)

    return (cnts * 1.0) / times


if __name__ == "__main__":
    t0 = time()
    res = solve(times=10**7)
    print("Final Result : {:.10f} . Time taken : {:.2f} secs.".format(
        res, time() - t0))
