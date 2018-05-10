'''
  P250

  Find the number of non-empty subsets of {1**1, 2**2, 3**3,..., 250250**250250}, 
  the sum of whose elements is divisible by 250. 
  
  Enter the rightmost 16 digits as your answer.
'''

from collections import defaultdict


def p250():
    res = 0
    count = defaultdict(int)

    for i in range(1, 250251):
        p = pow(i, i, 250)
        count[p] += 1

    print("#of reminders : ", len(list(count.keys())))
    return res


if __name__ == "__main__":
    res = p250()
    print(res)
