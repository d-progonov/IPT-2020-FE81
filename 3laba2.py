import math

n1 = 1

if __name__ == "__main__":

    # input data
    while True:
        n = input("Количество элементов n: ")
        try:
            n1 = int(n)
        except (TypeError, ValueError):
            print('Это не целое число или не число вообще')
            continue
        if n1 < 0:
            print("Невозможно выполнить действия с отрицательным числом. Введите другое число.")
        elif n1 == 0:
            print("Невозможно выполнить действия с 0. Введите другое число.")
        else:
            print('Число n = ', n1)
            break

    for i in range(1, n1 + 1):
        try:
            if 5 - 3*i > 0:
                print("Члены ряда, которые подходят:", i)
        except TypeError:
            print("Type Error")
            break
