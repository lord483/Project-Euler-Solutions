'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?  '''

num = 600851475143

for i in range(2, 10000):
    if num % i == 0:
        print(i)
        num = num / i
        print("new num = ", num)
