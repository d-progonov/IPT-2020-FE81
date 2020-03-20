def get_values():
    a = input('a = ')
    b = input('b = ')
    return a, b

def valid(num):
    try:
        float(num)
    except ValueError:
        print('Bad input !')
        exit()
    return True


def main():
    a, b = get_values()
    if valid(a) and valid(b):
        a, b = float(a), float(b)
        if a > b:
            print('Больше')
        elif b > a:
            print('mеньше')
        else:
            print('Эти числа равны')


if __name__ == '__main__':
    main()
