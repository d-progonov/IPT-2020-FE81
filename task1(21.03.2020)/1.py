def get_num():
    return input('Write number:\n')

def valid(num):
    if len(num) != 5:
        print('It must be 5 digits number')
        return False
    try:
        int(num)
    except ValueError:
        print('Bad input')
        return False
    return True

def main():
    a = get_num()
    if valid(a):
        for ch in a:
            print(ch)


if __name__ == '__main__':
    main()
