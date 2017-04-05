'''
    Problem 89 Roman numerals
'''
import roman


def toDec(r):
    num_list = [rd[c] for c in r]
    for i in range(len(num_list) - 1):
        if num_list[i] < num_list[i + 1]:
            num_list[i] *= -1
    return sum(num_list)

if __name__ == "__main__":
    rd = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    f = open("p089_roman.txt")
    for line in f:
        original_roman = line.strip()
        num = toDec(original_roman)
        new_roman = roman.toRoman(num)
        diff = len(original_roman) - len(new_roman)
        if diff > 0:
            res += diff

    print(res)
