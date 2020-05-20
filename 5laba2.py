import math


def getNSum(n, elem, step):
    if n == 1:
        return elem
    else:
        return elem+(n-1)*step+getNSum(n-1, elem, step)


if __name__ == "__main__":


    while True:
        inpStartElem = input("Введите начальный член прогрессии: ")
        try:
            f_Elem = float(inpStartElem)
            if math.isnan(f_Elem):
                print("Начальный член не может быть не числом (NAN).")
                continue
            elif math.isinf(f_Elem):
                print("Начальный член не может быть бесконечностью.")
                continue
        except ValueError:
            print("Скорее всего вы ввели не число.")
            continue
        break

    while True:
        inpStep = input("Введите шаг прогрессии: ")
        try:
            f_Step = float(inpStep)
            if math.isnan(f_Step):
                print("Шаг не может быть не числом (NAN).")
                continue
            elif math.isinf(f_Step):
                print("Шаг не может быть бесконечностью.")
                continue
            elif f_Step == 0:
                print("При шаге равному 0 прогрессия не будет изменяться, а состоять будет из одного числа:\n {0}".format(f_Elem))
                continue
        except ValueError:
            print("Скорее всего вы ввели не число.")
            continue
        break

    while True:
        inNum = input("Введите n: ")
        try:
            i_N = int(inNum)
            if i_N <= 0:
                print("Число членов прогрессии должно быть положительным.")
                continue
        except ValueError:
            print("Скорее всего вы ввели не число.")
            continue
        break
    summ = getNSum(i_N, f_Elem, f_Step)
    print("Результат: {0}".format(summ))