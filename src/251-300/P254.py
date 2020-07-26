from time import time



new_lst = [0]
user_input = input("Enter query: ")
start_time = time()


def fact_calc():
    fact = 1
    for y in range(9):
        factor = fact * y
        fact += factor
        new_lst.append(fact)


fact_calc()


def sf(num):
    fact_digit_sum = 0

    for number in str(num):
        d = int(number)
        fact_digit = new_lst[d]
        fact_digit_sum += fact_digit
    return fact_digit_sum


def f_sum(f):
    d_sum = 0
    for digit in str(f):
        digit = int(digit)
        fact_of_digit = digit
        d_sum += fact_of_digit
    return d_sum


def g(i):
    param = 10 ** 18
    for _ in range(1, param):
        f_s = f_sum(sf(str(_)))
        if int(i) == f_s:
            return _
        else:
            continue


print(g(user_input))
end_time = time()
print(end_time - start_time)
