import math


def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Error, уведите целое или дробное число")
        check_help = False
    return check_help


def work():
    while 1:
        print("Уведите числа в порядке: 1 - x, 2 - y, 3 - z")
        x = input("x =  ")
        if check(x) == False:
            continue
        y = input("y =  ")
        if check(y) == False:
            continue
        z = input("z =  ")
        if check(z) == False:
            continue
        else:
            x = float(x)
            y = float(y)
            z = float(z)
            ans = math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))
            print("Ответ: {}".format(ans))


work()
