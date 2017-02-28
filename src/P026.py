'''
Reciprocal cycles
Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.  '''


def rec_cyc(a):
    #print("in rec_cyc , for : ", a)
    dec = []
    s = 10
    cyc = 0
    rems = [1]
    divided = True
    while(True):
        #print(s , dec)
        if s < a:
            dec.append(0)
            cyc = cyc + 1
            s = s * 10
        else:
            r = s % a
            f = int(s / a)
            dec.append(f)

            if r == 0:
                cyc = 0
                #print("Divided .. for " ,a , "  dec =", dec,"  rem = ", rems)
                break
            elif r in rems:
                rems.append(r)
                first_pos = 0
                for i in range(0, len(rems)):
                    if rems[i] == r:
                        first_pos = i + 1
                        break

                cyc = len(rems) - first_pos

                #print("Not divided ... for " ,a , "  dec =", dec,"  rem = ", rems , ", first_pos = " ,first_pos, " len(rems)=" , len(rems))
                break
            else:
                rems.append(r)
                s = r * 10
    return(cyc)

max_res = 0
max_int = 0

for i in range(2, 1000):
    r = rec_cyc(i)
    if r > max_res:
        max_res = r
        max_int = i
    #print("Result = " , i,r)

print("max_res ", max_res, "  max_int :", max_int)
