from lab1 import valid

def num_sign(a: float):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0


def print_sign(sign: int):
    if sign > 0:
        print('Num > 0')
    elif sign < 0:
        print('Num < 0')
    else:
        print('Num = 0')

def main():
    a = input('Num = ')
    if valid(a) == True:
        print_sign(num_sign(float(a)))


if __name__ == '__main__':
    main()
