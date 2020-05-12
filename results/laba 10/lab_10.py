import numpy as np


def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Ошибка, уведите целое или дробное число")
        check_help = False
    return check_help


def square(x1, x2, y1, y2):
    res_1 = abs(float((x1 * y2 - x2 * y1) / 2))
    return res_1


def work():
    while 1:
        n = input("Уведите количество точек:  ")
        if check(n) == False:
            continue
        if int(n) <= 1:
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
                mass.append((num_x, num_y))
                n -= 1
        print(mass)
        list.sort(mass)
        print(mass)
        x = []
        y = []
        for i in mass:
            x.append(i[0])
            y.append(i[1])
        print(x)
        print(y)

        k = np.size(x)
        res = 0
        for i in range(0, k, 1):
            if i == (k - 1):
                z.append(square(x[0], x[k - 1], y[1], y[k - 1]))
            else:
                z.append(square(x[i], x[i + 1], y[i], y[i + 1]))
            res += z[i]
        print("Площадь н-угольника ровняется: " + str(res))

        break


if __name__ == "__main__":
    work()
