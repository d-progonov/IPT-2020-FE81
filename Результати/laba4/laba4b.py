import numpy as np

leftSide = -1
rightSide = 1

if __name__ == "__main__":
    while True:
        inpOrder = input("Введите количество элементов массива(натуральное число): ")
        try:
            order = int(inpOrder)

            if order == 0:
                print("НОЛЬ - это не натуральное число.")
                exit(-1)
            elif order < 0:
                print("Отрицательное число - это НЕ натуральное число.")
                continue
            break
        except ValueError:
            print("Похоже, вы ввели не число. Попытайтесь ещё раз.")
    array = [0] * order
    for i in range(order):
        array[i] = np.random.randint(leftSide, rightSide)

    print("Созданный массив: ")
    print(array)

    for i in range(len(array)):
        if array[i] == 0:
            del array[i]
            break

    for i in range(len(array)):
        if array[i] % 2 == 0:
            array.insert(i+1, array[i-1]+2)
            break

    print("Полученный массив: ")
    print(array)
