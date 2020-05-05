import sys, os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from include.usefullFuncs import check_input_data


def lab4_1():
    print("HI! Lab4!")
    x = input("Input x: ")
    size = check_input_data(1, x)

    A = np.arange((size ** 2)).reshape(size, size)

    print(A)

    middle = int(size / 2)
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


class Circle:

    def __init__(self, foo):
        """Constructor"""
        self.foo = foo
        self.size = len(foo)

    def get(self, n):
        num = n % self.size
        return self.foo[num]

    def remove(self, n):
        num = n % self.size
        print("removing ", self.foo[num])
        del self.foo[num]
        self.size = self.size - 1


def lab4_2():
    foo = [0, 1, 2, 3, 4, 5, 6, 7]

    circle = Circle(foo)

    #print(circle.get(10))

    for i in range(len(foo)+10, 10, -1):
        print(circle.get(i))

    circle.remove(7)
    circle.remove(7)

    for i in range(10, len(foo)+10, 1):
        print(circle.get(i))


print(lab4_1())
print(lab4_2())
