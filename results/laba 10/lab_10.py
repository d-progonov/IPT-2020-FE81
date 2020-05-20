import math
import operator
from functools import reduce


def check_help(NUM):
    check_help = True
    try:
        num_1 = int(NUM)
    except Exception:
        print("Ошибка! Уведите целое число")
        check_help = False
    return check_help


def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except Exception:
        print("Ошибка! Уведите целое или дробное число")
        check_help = False
    return check_help


def square(mass):
    n = len(mass)
    S = 0
    for i in range(0, n):
        x1 = mass[i][0]
        y1 = mass[i][1]
        x2 = mass[(i + 1) % n][0]
        y2 = mass[(i + 1) % n][1]
        S += x1 * y2 - x2 * y1
    res = abs(S / 2)
    return res


def func(a, b, c):
    ch = False
    if ((b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])) < 0:
        ch = True
    if ((b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])) > 0:
        ch = False
    return ch


def scan(mass):
    S = [mass[0], mass[1]]
    for i in range(2, len(mass)):
        while func(S[-2], S[-1], mass[i]) == True:
            del S[-1]
        S.append(mass[i])
    return S


def work():
    while 1:
        n = input("Уведите количество точек:  ")
        if check_help(n) == False:
            continue
        if int(n) <= 0:
            print("Ошибка, невозможно такое количество точек")
            continue
        else:
            n = int(n)
            mass = []
            z = []
        while n > 0:
            num_x = input("Уведите число x: ")
            if check(num_x) == False:
                continue
            num_y = input("Уведите число y: ")
            if check(num_y) == False:
                continue
            else:
                num_x = float(num_x)
                num_y = float(num_y)
                mass.append([num_x, num_y])
                n -= 1
        print(mass)
        # center = tuple(map(operator.truediv, reduce(lambda x, y: map(operator.add, x, y), mass), [len(mass)] * 2))
        center = min(mass)
        center = [center[0] - 1, center[1] + 0.11]
        print(center)
        mass_2 = sorted(mass, key=lambda coord: (-135 - math.degrees(
            math.atan2(*tuple(map(operator.sub, coord, center))[::1]))) % 360)
        print(mass_2)
        if len(mass_2) == 1:
            S = 0
            print("Площадь многоугольника:", S)
            break
        else:
            mass_3 = scan(mass_2)
            print(mass_3)
            S = square(mass_3)
            print("Площадь многоугольника:", S)
            break


if __name__ == "__main__":
    work()
