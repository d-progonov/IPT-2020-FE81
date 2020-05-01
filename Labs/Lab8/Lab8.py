import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def Cardi():
    a = int(input("Enter A:"))
    if a < 0:
        print(" 'a' must be above zero.")
        return
    else:
        t = np.arange(0.0, 2.0*np.pi, 0.01)

        x = (a*np.cos(t))*(1 + np.cos(t)) 
        y =  (a*np.sin(t))*(1 + np.cos(t))

        fig, ax = plt.subplots()
        ax.plot(x, y)

        ax.set(xlabel='x', ylabel='y',
            title='Сardioida')
        ax.grid()

        fig.savefig("cardi.png")
        plt.show()

Cardi()