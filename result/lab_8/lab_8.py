import matplotlib.pyplot as plt                                
from numpy import arange                                       
while (True):
    try:
        a=float(input("Enter a="))
        break
    except ValueError:
        print("Wrong data type of a")
while (True):
    try:
        d=float(input("Enter d="))
        break
    except ValueError:
        print("Wrong data type of d")
while (True):
    try:
        xmin = float (input("Enter left limit for x = ")) 
        break
    except ValueError:
        print("Wrong data type of left limit for x")
while (True):
    try:
        xmax = float (input("Enter right limit for x = ")) 
        break
    except ValueError:
        print("Wrong data type of right limit for x")

def func(a, d, x):               
    if ((d*x-2)) == 0:             
        return                     
    return ((a*x+3)/(d*x-2))        


figure, plot = plt.subplots()   
dx=0.001                               
xlist = arange(xmin, xmax, dx)          
ylist = [func(a, d, x) for x in xlist]
plot.plot(xlist, ylist, color = 'red', zorder = 5)
plt.xlabel('x', fontsize=15)                       
plt.ylabel('y', fontsize=15)
plot.set_title('y = (a*x+3)/(d*x-2)', fontsize=15)
plot.minorticks_on()
plot.grid(which='major', linestyle = 'dashed', color = 'blue')
plot.grid(which='minor', linestyle = 'dotted', color = 'cyan')
figure.set_facecolor('ivory')
if d!=0:
    ylim = plot.get_ylim()
    plt.vlines(2/d, ylim[0], ylim[1],linewidth = 2, zorder = 6)
plt.show()                                         

