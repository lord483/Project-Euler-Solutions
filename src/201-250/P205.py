'''
P205 

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? 

Give your answer rounded to seven decimal places in the form 0.abcdefg
'''

from itertools import product
from collections import defaultdict

if __name__ == "__main__":
    total = (4**9) * (6**6)
    print("Total #of permutations: ", total)
    peter = 0

    pyramids = [[1, 2, 3, 4]] * 9
    cubes = [[i for i in range(1, 7)]] * 6

    p_sum = defaultdict(int)
    for tup in product(*pyramids):
        s = sum(tup)
        p_sum[s] += 1

    c_sum = defaultdict(int)
    for tup in product(*cubes):
        s = sum(tup)
        c_sum[s] += 1

    # print(p_sum)
    # print(c_sum)

    # print(sum(p_sum.values()) * sum(c_sum.values()))

    pk = list(p_sum.keys())
    ck = list(c_sum.keys())

    for a, b in product(pk, ck):
        if a > b:
            peter += p_sum[a] * c_sum[b]

    print("Peter wins {} times out of total {} , with probability : {:.7f}".format(
        peter, total, peter / total))
