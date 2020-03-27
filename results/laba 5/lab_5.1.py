import numpy as np


def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Error, уведите целое или дробное число")
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
        if int(n) <= 0:
            print("Ошибка, невозможно такое количество чисел")
            continue
        if int(n) == 1:
            sqr = 0
        else:
            n = int(n)
            x = []
            y = []
            z = []
            sqr = 0
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
                x.append(num_x)
                y.append(num_y)
                print(x, y, sep='\n')
                n -= 1
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