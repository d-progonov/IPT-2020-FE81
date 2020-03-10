import math

################################################
#              Part A
###############################################

def create_primes_list(num,lst, pos):
    if lst[pos] > math.sqrt(num) + 1:    #All prime divisors less than sqrt(num)
        return lst
    else:
        lst = list(n for n in lst if (n % lst[pos] != 0 or n == lst[pos]))
        pos += 1
        return create_primes_list(num,lst,pos)


def list_in_file(lst, fl): #File is exists and was opened
    for i in lst:
        fl.write(str(i) + ',')
def file_to_list(fl):  # returns int`s list
    for line in fl:
        temp = line.split(',')
    return list(int(n) for n in temp if bool(n) == True)


def get_primes(num):
    try:
        primes_file = open('primes','r')
        primes = file_to_list(primes_file)
        primes_file.close()
        return primes
    except FileNotFoundError:
        print('Creating primes list...Wait!\nNext time it is must be faster')
        primes = create_primes_list(num, list(range(2,num)), 0)
        primes_file = open('primes', 'w')
        list_in_file(primes, primes_file)
        primes_file.close()
        return primes



def get_answer(num, primes_list):
    base_prime = primes_list[0]
    currnet_index = 0
    while base_prime < num:
        poss_prime = num - base_prime
        if poss_prime in primes_list:
            return(base_prime, poss_prime)
        else:
            currnet_index += 1
        base_prime = primes_list[currnet_index]


def valid_n(n):
    try:
        int(n)
    except ValueError:
        print('Bad input !')
        return False
    if int(n) <= 2 or int(n) > 1e+6:
        print('n is in bad domain !\n(2 < n < 1000000)')
        return False
    if int(n) % 2 != 0:
        print('n must be even !')
        return False
    return True

################################################
#              Part B
###############################################


def valid_power(power):
    try:
        int(power)
    except ValueError:
        print('Bad input !')
        return False
    if int(power) < 0:
        print('Power must be >= 0')
        return False
    if int(power) > 200:
        print('Power must be < 200 !')
    return True


def valid_num(num):
    try:
        float(num)
    except ValueError:
        print('Bad input !')
        return False
    if float(num) == 0:
        print('Num = 0 !')
        return False
    if float(num) < -10000 or float(num) > 10000:
        print('Num is in bad domain !')
        return False
    return True


def pow_(num, power, base):
    if power == 1:
        return num
    elif power == 0:
        return 1
    else:
        return pow_(num * base, power - 1, base)


def main():
    print("###########\nPart A\n###########")
    primes = get_primes(1000000)
    n = input('n = ')
    if valid_n(n) == True:
        n = int(n)
        a,b = get_answer(n, primes)
        print('%i = %i + %i' %(n, a, b))
    print("###########\nPart B\n###########")
    num = input('Num = ')
    power = input('Power = ')
    if valid_num(num) == True and valid_power(power) == True:
        num = float(num)
        power = int(power)
        try:
            print('%f^%i = %f' % (num, power, pow_(num,power,num)))
        except:
            print('Something went wrong, try again.')


if __name__ == '__main__':
    main()
