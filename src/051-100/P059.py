import numpy as np
import string


def solve(ip):
    global cnt
    cipher = np.asarray(ip)
    l = len(ip)
    f = (len(ip) // 3 + 1)
    for i in string.ascii_lowercase:
        for j in string.ascii_lowercase:
            for k in string.ascii_lowercase:
                key = [ord(i), ord(j), ord(k)] * f
                key = np.asarray(key[:l])
                pt = cipher ^ key
                check(pt)

    return 0


def check(pt):
    global cnt, cnt_space, cnt_cntrl, cnt_127
    # check for space
    c0 = pt == 32
    if np.sum(c0) <= 200:
        cnt_space += 1
        return False

    # filter control characters
    c1 = pt <= 31
    if np.sum(c1) > 0:
        cnt_cntrl += 1
        return False

    # filter non printable characters
    c2 = pt >= 127
    if np.sum(c2) > 0:
        cnt_127 += 1
        return False

    cnt += 1
    if cnt <= 30:
        print(pt.shape)
        st = [chr(c) for c in pt]
        print("\n" + "".join(st) + "\n")
        print(np.sum(pt), np.sum(c0))

    return


if __name__ == "__main__":
    ip = []
    cnt, cnt_space, cnt_cntrl, cnt_127 = 0, 0, 0, 0
    with open('p059_cipher.txt') as f:
        for line in f:
            ip.extend(list(map(int, line.split(","))))

    print("len(ip) : ", len(ip))

    solve(ip)
    print("cnt,cnt_space,cnt_cntrl,cnt_127 :  ", cnt, cnt_space, cnt_cntrl,
          cnt_127)
