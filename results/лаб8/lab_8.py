import matplotlib.pyplot as plt

while True:
     try:
          left_x = int(input("Input left boundary for 'x':"))
          break
     except ValueError:
          print("Invalid value entered!")

while True:
     try:
          right_x = int(input("Input right boundary for 'x':"))
          if right_x < left_x:
               print("Right boundary can't be less than left! Please, input another one:")
               continue
          break
     except ValueError:
                print("Invalid value enteredl")

while True:
        try:
                left_y = int(input("Input left boundary for 'y':"))
                break
        except ValueError:
                print("Invalid value entered!")

while True:
        try:
                right_y = int(input("Input right boundary for 'y':"))
                if right_y < left_y:
                         print("Right boundary can't be less than left! Please, input another one:")
                         continue
                break
        except Valuetrror:
                print("Invalid value entered!")

x_coord = list()
y_coord = list()

if __name__ == '__main__':
        for x in range(left_x, right_x + 1):
                for y in range(left_y, right_y + 1):
                        if abs(y) + 2 * abs(x) <= x ** 2 + 1:
                                x_coord.append(x)
                                y_coord.append(y)
                                print("The point is:", '(', x, ',', y, ')')

        plt.scatter(x_coord, y_coord, alpha=0.5)
        plt.title('Lab 8')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

        if len(x_coord) == len(y_coord) == 0:
                print("There are no points to satisfy your inequality!")
