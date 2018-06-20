'''
    Product-sum numbers
    Problem 88
'''

'''
Mathematical insights into the problem
    The first insight we should get is that if we have a set of factors,
    say {2,3,4} we get that 2*3*4 = 24 and 2+3+4 = 9. 
    
    Something that isn't exactly a product-sum like we are looking for. 
    However, we can add "ones" (1) which doesn't change the product but change the sum. 
    
    Indeed if we add 24-9 = 15 ones, we will get a product sum with 18 factors. 
    In other words any set of factors can be converted into a product-sum for , 
    
    k = “product of factor” – “sum of factors” + “number of factors”. 
    
    Whether this is minimal or not is another question.
'''


def prodsum(p, s, c, start):
    k = p - s + c     # product - sum + number of factors
    if k < kmax:
        if p < n[k]:
            n[k] = p
        for i in range(start, kmax // p * 2 + 1):
            prodsum(p * i, s + i, c + 1, i)


if __name__ == "__main__":
    kmax = 12000
    kmax += 1
    n = [2 * kmax] * kmax
    prodsum(1, 1, 1, 2)

    print("Project Euler 88 Solution =", sum(set(n[2:])))
