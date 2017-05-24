'''
    How many reversible numbers are there below one-billion?

    Note : It can be proven mathematically that there are no 9-digit , 5-digit or 1- Digit numbered solution.
          So we brute-force till 10**8
          It takes about 2.4 minutes
'''

from time import time


def solve(N):
    res_cnt = 0

    for i in range(12, N):
        si = str(i)
        if (si[-1] != '0') and (si[0] != si[-1]):
            rev = int(si[::-1])
            if rev > i:
                sums = str(i + rev)
                odd = True
                for c in sums:
                    if int(c) % 2 == 0:
                        odd = False
                        break
                if odd:
                    res_cnt += 2

    return res_cnt

if __name__ == "__main__":
    t0 = time()
    print(solve(10**8))
    print("Time taken : {:.3f} mins".format((time() - t0) / 60))
