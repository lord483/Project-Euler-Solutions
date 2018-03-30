'''
https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

'''

start = 2  # as 1 Jan 1901 = Tuesday

lm_fd = 6  # Last month first day as as 1 Dec 1900 = Saturday
tm_fd = 0

c = 0  # keep track of all matching cases

month = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
    'Nov', 'Dec'
]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for y in range(1901, 2001):
    for m in range(0, 12):
        d = 0
        if (m == 2) and (y % 4 == 0):
            d = 29
        else:
            d = days[m - 1]
        tm_fd = (lm_fd + d % 7) % 7
        if tm_fd == 0:
            c = c + 1
        #print( y , " " , month[m],"  ", tm_fd)
        lm_fd = tm_fd

print(c)
