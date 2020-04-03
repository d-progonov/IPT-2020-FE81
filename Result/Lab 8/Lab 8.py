import numpy
import matplotlib.pyplot as plot
from matplotlib import mlab
import math

def func(a, b, x):
    try:
        return ((a*x)/(b*(x**2)-3*x+1))
    except ZeroDivisionError:
        return math.inf


a = float(input('a = '))
d = float(input('d = '))
xmin = float(input('xmin = '))
xmax = float(input('xmax = '))
step = float(input('step = '))

x = []
y = []

for i in numpy.arange(xmin, xmax, step):
    x.append(i)
    y.append(func(a, d, i))

plot.plot(x, y)
plot.ylabel('Y')
plot.xlabel('X')
plot.show()
