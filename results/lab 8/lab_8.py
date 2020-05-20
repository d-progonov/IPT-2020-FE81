import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def RavlPask():
    a = int(input("Enter A:"))
    b = int(input("Enter B:"))
    if a <= 0 or b <= 0:
        print(" 'a and b ' must be above zero.")
        return
    else:
        t = np.arange(0.0, 2.0*np.pi, 0.01)

        x = (a*(np.cos(t)**2))+(b*(np.cos(t))) 
        y =  ((a*np.cos(t))*np.sin(t))+(b*(np.sin(t)))

        fig, ax = plt.subplots()
        ax.plot(x, y)

        ax.set(xlabel='x', ylabel='y',
            title='Ravlik')
        ax.grid()

        fig.savefig("ravl.png")
        plt.show()

RavlPask()