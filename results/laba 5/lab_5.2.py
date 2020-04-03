def g(n, a, c):
    res = (a * (n + c)) % 10
    return res


def f(n, *args):
    a = args[0]
    c = args[1]
    if n >= 0 and n <= 9:
        res = n
        return res
    else:
        res2 = g(n, a, c) * f(n - 1 - g(n, a, c), a, c) + n
        return res2


def work():
    while 1:
        try:
            m = int(input("Уведите число m:  "))
            if m < 0:
                raise ValueError
            break
        except ValueError:
            print("Ошибка, уведите целое или дробное натуральное число!")
    while 1:
        try:
            a = int(input("Уведите число а:  "))
            if a < 0:
                raise ValueError
            break
        except ValueError:
            print("Ошибка, уведите целое или дробное натуральное число!")
    while 1:
        try:
            c = int(input("Уведите число c:  "))
            if c < 0:
                raise ValueError
            break
        except ValueError:
            print("Ошибка, уведите целое или дробное натуральное число!")


    res = f(m, a, c)
    print("Остаточный результат:  " + str(res))


if __name__ == "__main__":
    work()
