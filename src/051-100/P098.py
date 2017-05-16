from collections import defaultdict, Counter


def compute_squares():
    global squares
    squares = [[[] for i in range(11)] for j in range(11)]

    for n in range(1, 10**5):
        m = n * n
        sm = str(m)
        lm = len(sm)
        um = len(set(sm))
        squares[lm][um].append(m)

    return


def find_anagrams():
    input_file = "p098_words.txt"
    d = defaultdict(list)
    anagrams = []
    with open(input_file) as fin:
        for line in fin:
            words = line.split(",")
            for w in words:
                word = w[1:-1]  # Remove double quotes
                l = [c for c in word]
                l.sort()
                key = "".join(l)
                d[key].append(word)

    for key in d.keys():
        if len(d[key]) > 1:
            anagrams.append(d[key])

    return anagrams


def check_pair(word1, word2):
    global squares
    l = len(word1)
    uc = len(set(word1))
    cc = Counter(word1)
    pattern_ = [cc[k] for k in cc.keys()]
    pattern_.sort()
    pattern = int("".join([str(count) for count in pattern_]))

    sl_ = squares[l][uc]

    if uc == l:
        sl = sl_
    else:
        sl = [n for n in sl_ if digit_pattern(n) == pattern]

    r = 0
    for n in sl:
        m = transform(word1, word2, n)
        if m in sl:
            r = max(r, n, m)

    return r


def digit_pattern(n):
    ns = str(n)
    cc = Counter(ns)
    p_ = [cc[k] for k in cc.keys()]
    p_.sort()
    p = int("".join([str(count) for count in p_]))

    return p


def transform(word1, word2, n):
    ns = str(n)
    mapper = dict()

    for c, digit in zip(word1, ns):
        if c in mapper:
            if mapper[c] != digit:
                return 0
        else:
            mapper[c] = digit

    return int("".join([str(mapper[c]) for c in word2]))

if __name__ == "__main__":
    anagrams = find_anagrams()
    compute_squares()
    print("Total pairs found ", len(anagrams))
    res = 0
    for pair in anagrams:
        if len(pair) == 2:
            res = max(res, check_pair(*pair))
        else:
            res = max(res, check_pair(*pair[:2]))
            res = max(res, check_pair(*pair[1:]))
            res = max(res, check_pair(pair[0], pair[2]))

    print(res)
