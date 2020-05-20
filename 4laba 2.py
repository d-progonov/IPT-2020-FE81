import random
if __name__ == "__main__":
    while True:
        inpOrder = input("Введите количество элеменов (натуральное число больше 5): ")
        try:
            order = int(inpOrder)

            if order < 5:
                print("Количество элементов не может быть меньше 5.")
                continue
            elif order < 0:
                print("Отрицательное число - это не натуральное число.")
                continue
            break
        except ValueError:
            print("Похоже, вы ввели не число. Попытайтесь ещё раз.")

    matrixA = [0]*order
    for i in range(order):
        matrixA[i] = random.randint(-1000, 1000)
    print(' '.join([str(elem) for elem in matrixA]))
    matrixB = matrixA.copy()
    del matrixB[0:5]
    x = [random.randint(-1000, 1000) for i in range(3)]
    matrixB.extend(x)

    print(' '.join([str(elem) for elem in matrixB]))