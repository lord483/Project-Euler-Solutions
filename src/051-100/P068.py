'''
    Problem 68 - Magic 5-gon ring
'''

from itertools import permutations
from time import time


def solve(n):
    res = 0
    l = list(range(1, n + 1))
    for a in permutations(l, r=None):
        t1 = [a[0], a[1], a[2]]
        t2 = [a[3], a[2], a[4]]
        t3 = [a[5], a[4], a[6]]
        t4 = [a[7], a[6], a[8]]
        t5 = [a[9], a[8], a[1]]

        s1 = sum(t1)
        s2 = sum(t2)
        s3 = sum(t3)
        s4 = sum(t4)
        s5 = sum(t5)

        if 10 in [a[1], a[2], a[4], a[6], a[8]]:
            continue
        if max((s1, s2, s3, s4, s5)) == min((s1, s2, s3, s4, s5)):
            order = [t1, t2, t3, t4, t5]
            outer_numbers = [(i, v[0]) for i, v in enumerate(order)]
            outer_numbers.sort(key=lambda x: x[1])
            start_index = outer_numbers[0][0]
            def_order = [i for i in range(5)]
            new_order = def_order[start_index:] + def_order[:start_index]

            num_arr = []
            for i in new_order:
                num_arr.extend(order[i])

            num_str = "".join(str(i) for i in num_arr)
            num = int(num_str)
            if num > res:
                res = num

    return res


if __name__ == "__main__":
    t0 = time()
    print(solve(10))
    print("Done in {:.2f} secs".format(time() - t0))
