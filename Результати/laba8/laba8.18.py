
import numpy as np

x_list = list()
y_list = list()

while True:
    try:
        l_bound_x = int(input("Input left boundary for 'x':"))
        break
    except ValueError:
        print("Invalid value entered!")

while True:
    try:
        r_bound_x = int(input("Input right boundary for 'x':"))
        if r_bound_x < l_bound_x:
            print("Right boundary can't be less than left! Please, input another one:")
            continue
        break
    except ValueError:
        print("Invalid value entered!")
        

while True:
    try:
        l_bound_y = int(input("Input lower boundary for 'y':"))
        break
    except ValueError:
        print("Invalid value entered!")

while True:
    try:
        r_bound_y = int(input("Input higher boundary for 'y':"))
        if r_bound_y < l_bound_y:
            print("Higher boundary can't be less than lower! Please, input another one:")
            continue
        break
    except ValueError:
        print("Invalid value entered!")
        
if __name__ == '__main__':
    for x in np.arange(l_bound_x, r_bound_x + 0.01, 0.01):
        for y in np.arange(l_bound_y, r_bound_y + 0.01, 0.01):
            if x * x + y * y <= 2 * (abs(x) + abs(y)):
                x_list.append(x)
                y_list.append(y)
                print("The point is:", '(', x, ',', y, ')')
                
    if len(x_list) == len(y_list) == 0:
        print("There are no points to satisfy your inequality!")
        
