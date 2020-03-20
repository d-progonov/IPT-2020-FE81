def valid_power(n):
    try:
        n = int(n)
        if n < 0 or n > 100:
            print('Bad input\n')
            exit()
    except ValueError:
        print('Bad input')
        exit()
    return True


def valid_num(k):
    try:
        k = float(k)
        if abs(k) > 10000:
            print('Bad input\n|k|<10000')
            exit()
    except ValueError:
        print('Bad input')
        exit()
    return True


def get_res(num, power):
    res = 1
    for i in range(0, power):
        res *=  num
    return res

def main():
    n = input('n = ')
    power = input('pow = ')
    if valid_num(n) and valid_power(power):
        n, power = float(n), int(power)
        print('%f^%f = %f' % (n, power, get_res(n, power)))



if __name__ == '__main__':
    main()
