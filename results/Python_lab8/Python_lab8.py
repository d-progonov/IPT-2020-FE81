import matplotlib.pyplot as plt
from numpy import arange
while(1):
    try:
        a = float (input("Enter a = "))
        xmin = float (input("Enter left limit for x = "))
        xmax = float (input("Enter right limit for x = "))
        break
    except ValueError:
        print("Wrong data type for variable (must be float).")

def func(a, x):
    if (a*(x**2)+2*x+1) == 0:
        return 
    return (1/(a*(x**2)+2*x+1))

f, ax = plt.subplots()
dx=0.0001
xlist = arange(xmin, xmax, dx)
ylist = [func(a, x) for x in xlist]
ax.plot(xlist, ylist)
plt.xlabel('x', fontsize=12)
ax.set_title('y = 1/(a*(x^2)+2*x+1)', fontsize=12)
ax.minorticks_on()
ax.grid(which='major', linestyle = '--')
ax.grid(which='minor', linestyle = ':')
plt.show()
input("Any key to exit...")