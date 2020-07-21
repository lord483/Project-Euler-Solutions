""" 
Digit power sum 

The number 512 is interesting because it is equal to the sum of its digits raised to some power: 
    5 + 1 + 2 = 8, and 8^3 = 512. 
Another example of a number with this property is 614656 = 28^4.

We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.
"""

def digitsum(p):

    return sum([int(x) for x in str(p)])

def p119(N=10):
    MAX = 10**20
    results = []
    for i in range(2,199):
        for j in range(2,30):
            p = i**j 
            if p > MAX:
                break
            if digitsum(p) == i:
                print(i, j, p)
                results.append(p)
    
    results.sort()
    print(f"Total number of solutions found : {len(results)}")
    print(results)

    if N > len(results):
        raise Exception(f"Could not find {N} samples within {MAX}")

    return results[N-1]


if __name__ == "__main__":
    r = p119(N=30)

    print("Final result : ", r)