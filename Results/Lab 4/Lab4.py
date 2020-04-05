import sys, os
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from include.usefullFuncs import check_input_data


def lab4():
    print("HI! Lab4!")
    x = input("Input x: ")
    size = check_input_data(1, x)

    A = np.arange((size ** 2)).reshape(size, size)

    print(A)

    middle = int(size/2)
    leftTop = A[:middle, :middle]
    rightTop = A[:middle, middle:size]
    leftBottom = A[middle:size, :middle]
    rightBottom = A[middle:size, middle:size]

    B = np.array(A)
    B[:middle, :middle] = leftBottom
    B[:middle, middle:size] = leftTop
    B[middle:size, middle:size] = rightTop
    B[middle:size, :middle] = rightBottom

    print(B)


print(lab4())