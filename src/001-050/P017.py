'''
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage. '''

words = []
for i in range(0, 1001):
    words.append(' ')

words[0:10] = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
words[11:20] = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
# print(words[0:21])

cent = 'hundred'
words[30] = 'thirty'
words[40] = 'forty'
words[50] = 'fifty'
words[60] = 'sixty'
words[70] = 'seventy'
words[80] = 'eighty'
words[90] = 'ninety'
words[100] = 'one hundred'
words[1000] = 'one thousand'

for i in range(21, 100):
    u = i % 10
    if u > 0:
        uc = words[u]
        words[i] = words[i - u] + '-' + uc
# print(words[21:51])

for i in range(101, 1000):
    w = ''
    dc = ''
    cc = ''
    c = int(i / 100)
    cc = words[c] + " " + cent

    d = i % 100
    if d != 0:
        dc = words[d]
        w = cc + " and " + dc
    else:
        w = cc
    words[i] = w


# Final calculation

def len_w(w):
    n = 0
    for c in w:
        if c not in [' ', '-']:
            n = n + 1
    return(n)

res = 0

for i in range(1, 1001):
    res = res + len_w(words[i])

print("result =", res)


print("all complete. Lets test.")

ip = int(input("eneter a number : "))
while(ip != 0):
    print("word = ", words[ip], "  lenght=", len_w(words[ip]))
    ip = int(input("eneter a number : "))
