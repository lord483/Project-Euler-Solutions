'''
Coin sums
Problem 31
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

count = 0
a1,a2,a3,a4,a5,a6,a7,a8=0,0,0,0,0,0,0,0

for e1 in range(0,201):
    for e2 in range(0,101):
        a2 = e1 + 2*e2
        if  a2 > 200:
            break
        for e3 in range(0,41):
            a3 = a2 + 5*e3
            if a3 >200:
                break
            for e4 in range(0,21):
                a4 = a3 + e4*10
                if a4>200:
                    break
                for e5 in range(0,11):
                    a5 = a4 + e5*20
                    if a5 > 200:
                        break
                    for e6 in range(0,5):
                        a6 = a5 + e6*50
                        if a6 > 200:
                            break
                        for e7 in range(0,3):
                            a7 = a6 + e7*100
                            if a7 > 200:
                                break
                            for e8 in [0,1]:
                                a8 = a7 + e8*200
                                if a8 == 200:
                                    count = count +1

print("result = ", count)
                    
                            
                    
