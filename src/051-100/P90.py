from itertools import product, combinations
digits = [i for i in range(10)]

squares = set([i * i for i in range(1, 10)])

print(squares)

if __name__ == "__main__":
    res = 0
    cnt = 0
    for left, right in product(
            combinations(digits, 6), combinations(digits, 6)):
        # print(left, right)
        left_set = set(left)
        right_set = set(right)

        if 6 in left_set:
            left_set.add(9)
        if 6 in right_set:
            right_set.add(9)
        if 9 in left_set:
            left_set.add(6)
        if 9 in right_set:
            right_set.add(6)

        all_comb = set(
            [a * 10 + b for a, b in product(list(left_set), list(right_set))])
        all_comb.update(
            set([
                b * 10 + a for a, b in product(
                    list(left_set), list(right_set))
            ]))

        # print(all_comb)

        if squares.issubset(all_comb):
            res += 1
        #
        cnt += 1
        # if cnt > 5:
        #     break

    print(res // 2)
    print(cnt)
