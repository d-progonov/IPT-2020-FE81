import math
from lab2 import num_sign
#Part A

def find_series_sum():
    sum = 0
    a = 1
    while a != 14:
        sum += math.log(math.factorial(a)) / (a ** 2)
        a += 1
    return sum



#################################################################
#################################################################
# Part b

def find_all_div(n: int):
    div_lst = list()
    div_lst.append(1)                           # n % 1 = 0
    for i in range(2, (int(math.sqrt(n)) + 2) ):# All divisors < n^(1/2)
        if n % i == 0:
            div_lst.append(i)
    div_lst.append(n)                           # n % n = 0
    return div_lst


def valid_n(n: str):
    try:
        int(n)
    except ValueError:
        print('Bad input!')
        exit()
    if float(n) > 10e+12:
        print('Num is too big, cant to compute it')
        exit()
    if num_sign(int(n)) != 1 or type(n) == float():
        print('n is not in N domain')
        exit()
    return True

def main():
    print('Sum of series ln(n!)/n^2 = %f' % find_series_sum())
    n = input('n = ')
    if valid_n(n) == True:
        print('All divisors of n: ')
        print(find_all_div(int(n)))



if __name__ == '__main__':
    main()
