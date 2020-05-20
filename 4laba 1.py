import random

if __name__ == "__main__":
    while True:
        inpOrder = input("Введите порядок матрицы (натуральное число): ")
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

    matrixB = [[0] * order for i in range(order)]
    for i in range(order):
        for j in range(order):
            matrixB[i][j] = random.randint(-1000, 1000)

    print("Матрица B: ")
    for row in matrixB:
        print(' '.join([str(elem) for elem in row]))

    matrixA = [[0] * order for i in range(order)]

    for i in range(order):
        for j in range(order):
            if matrixB[i][j] > matrixB[i][i]:
                matrixA[i][j] = 1

    print("Матрица A: ")
    for row in matrixA:
        print(' '.join([str(elem) for elem in row]))