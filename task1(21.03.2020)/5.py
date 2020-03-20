def get_values():
    a = input('a = ')
    b = input('b = ')
    c = input('c= ')
    return a, b, c

def valid(num):
    try:
        float(num)
    except ValueError:
        print('Bad input !')
        exit()
    return True

def main():
    a, b, c = get_values()
    if valid(a) and valid(b) and valid(c):
        a, b, c = float(a), float(b), float(c)
        if a==b or a==c or b==c:
            a, b, c = a+5, b+5, c+5
            print(a,b,c)
        else:
            print('Равных нет')

if __name__ == '__main__':
    main()
