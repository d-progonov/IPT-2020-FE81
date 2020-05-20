import matplotlib.pyplot as plt



while True:

     try:

          left_x = int(input("Введите левую границу для 'x':"))

          break

     except ValueError:

          print("Введено неверное значение")



while True:

     try:

          right_x = int(input("ВВедите правою границу для 'x':"))

          if right_x < left_x:

               print("Правая граница не может быть меньше левой:")

               continue

          break

     except ValueError:

                print("Неверное значение")



while True:

        try:

                left_y = int(input("Введите левую границу для 'y':"))

                break

        except ValueError:

                print("Неверное значение")



while True:

        try:

                right_y = int(input("Введите правое значение для 'y':"))

                if right_y < left_y:

                         print("Правое значение не может быть меньше левого:")

                         continue

                break

        except Valuetrror:

                print("Неверное значение")



x_coord = list()

y_coord = list()



if __name__ == '__main__':

        for x in range(left_x, right_x + 1):

                for y in range(left_y, right_y + 1):

                        if abs(y) + 2 * abs(x) <= x ** 2 + 1:

                                x_coord.append(x)

                                y_coord.append(y)

                                print("Точки:", '(', x, ',', y, ')')



        plt.scatter(x_coord, y_coord, alpha=0.5)

        plt.title('Lab 8')

        plt.xlabel('x')

        plt.ylabel('y')

        plt.show()



        if len(x_coord) == len(y_coord) == 0:

                print("Нет точек что бы удовлетворить неравенство")
                
