def valid_n(n):
    try:
        n = int(n)
        if n < 0 or n > 1e+4:
            print('Bad input\n0<N<+10000')
            exit()
    except ValueError:
        print('Bad input')
        exit()
    return True

def valid_k(k):
    try:
        k = float(k)
        if abs(k) > 10:
            print('Bad input\n|k|<10')
            exit()
    except ValueError:
        print('Bad input')
        exit()
    return True


def get_result(n, k):
    res = 0
    for num in range(1, n+1):
        res += num ** k
    return res

def main():
    n = input('n = ')
    k = input('k = ')
    if valid_n(n) and valid_k(k):
        print('Result: ', get_result(int(n), float(k)))


if __name__ == '__main__':
    main()
