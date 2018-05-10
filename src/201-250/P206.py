'''
    Problem 206 : Concealed Square
    
    Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
    where each “_” is a single digit.

'''


def solve_P206():
    start = 1020000000000000000
    a = int(start**0.5)
    a -= (a % 10)
    print("Starting from : ",  a)
    while(True):
        if is_concealed_sqr(a * a):
            return a
        a += 10


def is_concealed_sqr(n):
    s = str(n)
    if len(s) != 19:
        return False

    num = int("".join([s[i] for i in range(0, 19, 2)]))
    if num == 1234567890:
        return True

    return False


if __name__ == "__main__":
    # print(is_concealed_sqr(1223344556677889900))
    print(solve_P206())
