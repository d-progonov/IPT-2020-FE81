def valid_n(n):
    if len(n) != 2:
        print('Bad input')
        exit()
    try:
        n = int(n)
        if n <= 0:
            print('n !є N')
            exit()
    except ValueError:
        print('Bad input')
        exit()
    return True

def main():
    n = input('n = ')
    if valid_n(n):
        res_l = [int(digit) for digit in n]
        res_l = sorted(res_l)
        if res_l[0] ==  res_l[1]:
            print('Digits are equal')
        else:
            print('The smallest number is %i\nHighest digit is %i' % (res_l[0], res_l[1]))



if __name__ == '__main__':
    main()
