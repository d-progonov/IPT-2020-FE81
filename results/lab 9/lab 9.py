import matplotlib.pyplot as plt
import numpy as np
import random


class TShape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print("Draw " + self.name)

    def move(self, x, y):
        print("Move")

    def rotate(self):
        print("Rotate")

    def change_color(self, color):
        print("Changed color")


class TPoint(TShape):
    def __init__(self, x=None, y=None, color='g', count = 40):
        if x is None:
            x = [random.randint(-500, 500) for i in range(0, count)]
        if y is None:
            y = [random.randint(0, 500000) for i in range(0, count)]
        self.x = x
        self.y = y
        TShape.__init__(self, "Point")
        self.color = color
        self.graph = None

    def draw(self, ax):
        self.graph = ax.plot(self.x, self.y, 'o', color=self.color)
        # ax.setp(self.graph, color=self.color)

    def move(self, x, y, ax=None):
        for i in range(0, len(self.x)):
            self.x[i] += x
        for i in range(0, len(self.y)):
            self.y[i] += y
        if not ax == None:
            self.draw(ax)

    def change_color(self, color):
        print("Changed color")
        self.color = color


class TLine(TPoint):
    def __init__(self, color='r'):
        TShape.__init__(self, "Line")
        TPoint.__init__(self, np.arange(-500, 500, 1), [50 for i in range(0, 1000)], color)

    def draw(self, ax):
        self.graph = ax.plot(self.x, self.y, color=self.color)

    def rotate(self, ax=None):
        TPoint.__init__(self, self.y, self.x, self.color)
        if not ax == None:
            self.draw(ax)


class TPol(TLine):
    def __init__(self, points_num=1000, a=1.0, b=1.0, c=1.0, color='y', ):
        TShape.__init__(self, "TPol")
        x = np.arange(((-1) * points_num / 2), (points_num / 2), 1)
        TPoint.__init__(self, x, self.get_y(x, a, b, c), color)

    def get_y(self, x, a, b, c):
        y = []
        for i in x:
            y.append((a * (i ** 2)) + (b * i) + c)
        return y


class TPoly(TLine):
    def __init__(self, koefs=None, points_num=1000, color='b'):
        if koefs == None:
            koefs = [2.0, 1.0, 1.0]
        TShape.__init__(self, "TPoly")
        x = np.arange(((-1) * points_num / 2), (points_num / 2), 1)
        TPoint.__init__(self, x, self.get_y(x, koefs), color)
        self.koefs = koefs

    def get_y(self, x, koefs):
        y = []
        for i in x:
            num = 0
            stepen = len(koefs) - 1
            for k in koefs:
                num += k * (i ** stepen)
                stepen -= 1
            y.append(num)
        return y

    def mashtab(self, points_num, ax=None):
        x = np.arange(((-1) * points_num / 2), (points_num / 2), 1)
        TPoint.__init__(self, x, self.get_y(x, self.koefs), self.color)
        if not ax == None:
            self.draw(ax)


point = TPoint()
line = TLine()
pol = TPol()
poly = TPoly()

figs, (ax1, ax2) = plt.subplots(nrows=2, ncols=2)

point.draw(ax1[0])
line.draw(ax1[0])
pol.draw(ax1[0])
poly.draw(ax1[0])

line.rotate(ax1[1])
pol.rotate(ax1[1])
poly.rotate(ax1[1])

line.rotate()
pol.rotate()
poly.rotate()

point.change_color('r')
line.change_color('g')
pol.change_color('b')
poly.change_color('y')

point.move(1000, 0, ax2[0])
line.move(1000, 0, ax2[0])
pol.move(1000, 0, ax2[0])
poly.move(1000, 0, ax2[0])

poly.mashtab(10000, ax2[1])

plt.show()
