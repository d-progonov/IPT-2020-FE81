import math

def get_input():
    inpt = input('Write number to check or Enter to exit:\n')
    if len(inpt) == 0:
        exit()
    else:
        try:
            num = int(inpt)
            if num < 1 or num > 1e+6:
                raise ValueError
            return num
        except ValueError:
            print('Bad number !')
            return False



def create_primes_list(num, lst, pos = 0):
    if lst[pos] > math.sqrt(num) + 1:
        return lst
    else:
        lst = list(n for n in lst if (n % lst[pos] != 0 or n == lst[pos]))
        pos += 1
        return create_primes_list(num,lst,pos)

def main():
    primes_list = list()
    to_num = 0
    num = get_input()
    while True:
        if bool(num):
            if num > to_num:
                if num > 4e+5:
                    print('Computing....')
                primes_list = create_primes_list(num,list(range(2, num + 1)) )
                to_num = num
            if num in primes_list:
                print('{} IS prime'.format(num))
            else:
                print('{} is NOT prime'.format(num))
        num = get_input()
main()
