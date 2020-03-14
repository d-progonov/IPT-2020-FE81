import math


def check(NUM, POINT):
    check_help = True
    try:
        num = float(NUM)
    except ValueError:
        print("Error.a, уведите целое или дробное число")
        check_help = False
    try:
        point = float(POINT)
    except ValueError:
        print("Error.b, уведите целое или дробное число")
        check_help = False
    return check_help


def work():
    while 1:
        x = input("x=")
        a = input("a (у градусах) = ")
        if check(x, a) == False:
            continue
        else:
            x = float(x)
            a = float(a)
            a = math.radians(a)
            print(a)

            while a < 0:
                a = 2 * (math.pi)
            while a >= 2 * (math.pi):
                a -= 2 * (math.pi)
            print(a)

        try:
            ans = (math.log1p(x ** 3 - 8) + 1 / math.sin(a))
            print("Ответ: {}".format(ans))

        except ZeroDivisionError:
            print("Ошибка значения числа a, на 0 делить нельзя")
        except ValueError:
            print("Ошибка значения числа х, введите x заново")
        break

work()
