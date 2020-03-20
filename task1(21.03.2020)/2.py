def get_values(nms):
    try:
        res =  [float(x) for x in nms.split(',') if bool(x) == True]
        if len(res) != 3:
            print('Bad input !')
            exit()
        if res[0] == 0:
            print('Division by zero !')
            exit()
        return res
    except ValueError:
        print('Bad input !')
        exit()


def main():
    a, b, f = get_values(input('a, b, f = '))
    try:
        res = (a + b - (f / a)) + (f*a*a) - (a + b)
    except:
        print('Something went wrong')
    print('Result:', res)


if __name__ == '__main__':
    main()
