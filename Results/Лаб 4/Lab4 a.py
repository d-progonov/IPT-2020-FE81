temp = ''

b = []



if __name__ == '__main__':



    while True:

        try:

            while True:

                a = int(input("Введите размерность матрицы: "))

                if a < 1:

                    print("Количество елементов не может быть меньше 1")

                else:

                    break

        except ValueError:

            print("Неверное значение")

        else:

            break



    matrix = [[0] * a for i in range(a)]



    for i in range(a):

        print("raw", i+1)

        for j in range(a):

            while True:

                try:

                    while True:

                        matrix[i][j] = int(input())

                        if matrix[i][j] <= 100:

                            break

                        else:

                            print("Количество елементов не может быть больше 100")

                except ValueError:

                    print("Неверное значение")

                else:

                    break

    for i in range(a):

        for j in range(a):

            print(matrix[i][j], end='   ')

        print()



    for i in range(a):

        for j in range(a):

            temp = temp + str(matrix[j][i])

        if temp == temp[::-1]:

            b.append(1)

        else:

            b.append(0)

        temp = ''



    print(b)
