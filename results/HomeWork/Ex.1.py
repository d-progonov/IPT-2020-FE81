def check(x):
    check_help = True
    try:
        num_1 = float(x)
    except ValueError:
        print("Введите целое или дробное число")
        check_help = False
    return check_help


def work():
    while 1:
        x = input("Введите целое или дробное число (5 розрядов)")
        if check(x) == False:
            continue
        if abs(int(x)) == False:
            continue
        if abs(int(x)) < 10000:
            continue
        if abs(int(x)) > 99999:
            continue
        else:
            x = abs(float(x))
            i = 10000
            while (i >= 1):
                print(int(((x - (x % i)) / i) % 10))
                i /= 10
        break


work()