
def solve(n):
    mem = [0 for _ in range(n + 1)]
    mem[0] = 1
    for i in range(1, n):
        for j in range(i, n + 1):
            mem[j] += mem[j - i]

    return mem[-1]

if __name__ == "__main__":
    n = 100
    print(solve(n))
