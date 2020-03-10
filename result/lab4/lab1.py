def get_data():
    a = input('a = ')
    b = input('b = ')
    return (a, b)


def valid(a: str):
    try:
        a = float(a)
        if a > 10e+50:
            print('Values too big, cant to compute it !')
            return False
        return True
    except ValueError:
        print('Bad input !')
        exit()


def get_fun_val(a: float, b: float):
    try:
        return  ( ((a-b) **  5) / ((b-a) ** 3) ) ** (1/2)
    except ZeroDivisionError:
        print("Division by zero !")
        exit()
    except:
        print("Something went wrong, try again.")
        exit()


def print_result(result):
    if type(result) == complex:
        print('f(a,b) = %f + i(%f) ' %  (result.real, result.imag))
    elif type(result) == float:
        print('f(a,b) = %f ' % result)
    else:
        raise TypeError
        exit()


def main():
    a,b = get_data()
    if valid(a) == True and valid(b) == True:
        fun_val = get_fun_val(float(a),float(b))
        print_result(fun_val)


if __name__ == '__main__':
    main()
