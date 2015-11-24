'''
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?   '''

n = 1001

#initize array
a=[]
for i in range(0,n):
    row = [j-j for j in range(0,n)]
    a.append(row)
'''
for row in a:
    print(row) '''

#load array

x=int((n-1)/2)
y=int((n-1)/2)
level = 0
x0 = 0
y0 = 0

for num in range(1,(n*n)+1):
    i = y - y0
    j = x + x0
    a[i][j] = num
    if i == 0 and j == n-1:
        break
    if x0 == level and y0 == level:
        level = level + 1
        x0= x0 + 1
    elif x0 == level and y0 < level and y0 > level*(-1):
        y0 = y0 - 1
    elif x0 == level and ( y0 == level*(-1) ):
        x0=x0-1
    elif (x0 < level) and (x0 > level*(-1)) and (y0 == level*(-1)):
        x0=x0-1
    elif (x0 == level*(-1)) and (y0 == level*(-1)):
        y0 = y0 + 1
    elif (x0 == level*(-1)) and (y0 > level*(-1)) and y0 < level:
        y0 = y0 + 1
    elif (x0 == level*(-1)) and y0 == level:
        x0=x0+1
    elif (x0 >  level*(-1)) and y0 == level and (x0 < level):
        x0=x0+1
    '''
    print("===  step   ====", num)
    for row in a:
        print(row)
    print(" ") '''
    
'''
for row in a:
    print(row) '''

# sum diagonally

s = 0
for i in range (0,n):
    s = s + a[i][i]+a[n-1-i][i]
s = s - 1
print(s)
    
        

        
        
        
        
    


