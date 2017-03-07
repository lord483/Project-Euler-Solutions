'''
Lexicographic permutations
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?    '''

m1 = set(range(0, 10))
print(m1)

'''
m2 = m1 - {0}

print(m2) '''

count = 0

for e1 in m1:
    print("now e1 = ", e1)
    if count >= 1000000:
        break
    m2 = m1 - {e1}
    for e2 in m2:
        print("now e2 = ", e2)
        if count >= 1000000:
            break
        m3 = m2 - {e2}
        for e3 in m3:
            if count >= 1000000:
                break
            m4 = m3 - {e3}
            for e4 in m4:
                if count >= 1000000:
                    break
                m5 = m4 - {e4}
                for e5 in m5:
                    m6 = m5 - {e5}
                    for e6 in m6:
                        m7 = m6 - {e6}
                        for e7 in m7:
                            m8 = m7 - {e7}
                            for e8 in m8:
                                m9 = m8 - {e8}
                                for e9 in m9:
                                    m10 = m9 - {e9}
                                    for e10 in m10:
                                        count = count + 1
                                        if count == 1000000:
                                            s = ''
                                            s = str(e1) + str(e2) + str(e3) + str(e4) + str(e5) + str(e6) + str(e7) + str(e8) + str(e9) + str(e10)
                                            print(s)
                                            break

print("count =", count)
