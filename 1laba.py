import math

while True:
    a = str(input("Введите число a: "))
    try:
        a1 = float(a)
        print('Число а = ', a1)
        break
    except (TypeError, ValueError):
        print('Это не число')


while True:
    b = str(input("Введите число b: "))
    try:
        b1 = float(b)
        print('Число b = ', b1)
        break
    except (TypeError, ValueError):
        print('Это не число')


while True:
    x = str(input("Введите число x: "))
    try:
        x1 = float(x)
        print('Число x = ', x1)
        break
    except (TypeError, ValueError):
        print('Это не число')

c = (a1*x1 + b1)


def sign(c):
    if c < 0:
        return -1
    elif c > 0:
        return 1
    else:
        return 0


def calc(b1, x1, c):
    if (sign(c) - math.fabs(x1 - b1)) >= 0:
        print("Ответ:", (sign(c) - math.fabs(x1 - b1))**(1/2))
    else:
        print("Числа не входят в область допустимых значений")


print("Значение функции sign:", sign(c))

calc(b1, x1, c)