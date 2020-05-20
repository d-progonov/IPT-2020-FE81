temp = ''

b = []



if __name__ == '__main__':



    while True:

        try:

            while True:

                n = int(input("Enter dimension of matrix: "))

                if n < 1:

                    print("number of elements can not be less than 1")

                else:

                    break

        except ValueError:

            print("Invalid value")

        else:

            break



    matrix = [[0] * n for i in range(n)]



    for i in range(n):

        print("raw", i+1)

        for j in range(n):

            while True:

                try:

                    while True:

                        matrix[i][j] = int(input())

                        if matrix[i][j] <= 9:

                            break

                        else:

                            print("item must be less than 9")

                except ValueError:

                    print("Invalid value")

                else:

                    break

    for i in range(n):

        for j in range(n):

            print(matrix[i][j], end='   ')

        print()



    for i in range(n):

        for j in range(n):

            temp = temp + str(matrix[j][i])

        if temp == temp[::-1]:

            b.append(1)

        else:

            b.append(0)

        temp = ''



    print(b)

      

  
