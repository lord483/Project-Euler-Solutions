'''
    Multiples with small digits
    Problem 303
'''
from itertools import product
from time import time


def solve(m):
    res = 2  # FOr 1 :  1*1=1 , for 2 : 2*1 = 2

    for n in range(3, m + 1):
        v = P303(n)
        if v > 0:
            print(n, v)
        res += v
    return res


def P303(n):
    digits = [int(c) for c in str(n)]
    if all((d <= 2 for d in digits)):
        return 1

    num_digits = len(digits)

    while(True):
        s = [["1", "2"]] + [["0", "1", "2"]] * (num_digits - 1)
        for p in product(*s):
            num = int("".join(p))
            if num % n == 0:
                return num // n
        num_digits += 1

    return 0


if __name__ == '__main__':
    '''
        Note : SLow !! Takes about 35 mins for 10**4 !

    '''
    t0 = time()
    res = solve(10**4)
    print("\nFinal Result : {}\n".format(res))
    print("Time taken {:.2f} secs".format(time() - t0))
