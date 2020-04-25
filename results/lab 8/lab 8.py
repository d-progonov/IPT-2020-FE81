from pylab import plot, show
from math import sin, cos, pi
n=range(100)
t=[2*pi*i/100 for i in n]
x=[cos(t[i])**3 for i in n]
y=[sin(t[i])**3 for i in n]
plot(x, y, 'r-')
show()