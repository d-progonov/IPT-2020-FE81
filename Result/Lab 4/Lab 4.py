import math
import numpy as np


if __name__ == '__main__':
    while True:
        try:
            size = int(input("Input array size:"))
            if size <= 3:
                print("Please, input another value > 3!")
                continue
            if size == 0:
                print("Matrix can`t exist at this size!")
            break
        except ValueError:
            print("Invalid value entered!")


    matrix = np.array([[i + 1 for i in range(size)] for _ in range(size)])
    array = np.array([[0 for i in range(size)] for _ in range(size)])

    for i in range(size):
        for k in range(0,size - i):
            array[i][k]=matrix[i][k+i]

    print(array)
