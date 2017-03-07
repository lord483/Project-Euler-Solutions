'''
Combinatoric selections
Problem 53
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?   '''


def ncr(n, b):
    # find if ncr > 1mil
    k = n - b
    r = min(b, k)
    k = n - r
    ul = [i for i in range(k + 1, n + 1)]
    bl = [i for i in range(2, r + 1)]

    for i in range(len(bl)):
        b = bl[i]
        for j in range(len(ul)):
            if ul[j] % b == 0:
                ul[j] = ul[j] / b
                bl[i] = 1
                break
    m = 1
    b = 1

    for i in bl:
        b = b * i

    for i in ul:
        m = m * i
        if b > 1 and m > b:
            m = m / b
            b = 1

        if m > 1000000 and b == 1:
            return True

    return False
    # return m


def main():
    '''
    while(True):
        n = input("Enter n : ")
        r = input("Enter r : ")
        print(ncr(int(n),int(r)))

    '''
    count = 0
    for i in range(5, 101):
        for j in range(2, i):
            if ncr(i, j):
                l = i - j
                if l < j:
                    count = count + 1
                else:
                    count = count + l - j + 1

                print(i, ' ', j, ' ', count)
                break
    print("result = ", count)


if __name__ == '__main__':
    main()
