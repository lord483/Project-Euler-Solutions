
from time import time
all_num = set([i for i in range(1, 10)])

def solve_sudoku(ip):
    blanks = []
    for i in range(9):
        for j in range(9):
            if ip[i][j] == 0:
                blanks.append((i, j))

    nb = len(blanks)
    index = 0
    while 0 <= index < nb:
        x, y = blanks[index]
        v = ip[x][y]
        if v == 9:
            ip[x][y] = 0
            index -= 1
        else:
            rem = check(ip, x, y)
            found = 0
            if rem:
                for r in rem:
                    if r > v:
                        found = r
                        break

            if found:
                ip[x][y] = found
                index += 1
            else:
                ip[x][y] = 0
                index -= 1

    return ip

def check(ip, x, y):
    s = set([ip[i][y] for i in range(9) if i != x])
    s.update([ip[x][j] for j in range(9) if j != y])

    l, t = 0, 0
    l = y - (y % 3)
    t = x - (x % 3)

    for i in range(t, t + 3):
        for j in range(l, l + 3):
            if (i != x) and (j != y):
                s.add(ip[i][j])

    rem = list(all_num.difference(s))
    rem.sort()

    return rem


if __name__ == "__main__":
    input_file = "p096_sudoku.txt"
    f = open(input_file)
    ip = []
    cnt = 0
    res = 0
    header = ""
    start_time = time()

    for line in f:
        cnt += 1
        if cnt == 1:
            header = line.strip()
            t0 = time()
        else:
            ip.append([int(c) for c in line.strip()])

        if cnt == 10:
            solution = solve_sudoku(ip)
            a, b, c = solution[0][:3]
            print("\n Solved {} , time taken {:.3f} secs".format(header, time() - t0))
            # Print solution
            for row in solution:
                print(row)
            res += (100 * a + 10 * b + c)
            cnt = 0
            ip = []

    print("\n Final Result :", res)
    print("Total time taken : {:.3f} secs".format(time() - start_time))
