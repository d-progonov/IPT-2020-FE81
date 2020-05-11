import matplotlib.pyplot as plt
import numpy as np

a=input("Enter a:")
b=input("Enter b:")

try:
    a=int(a)
    b=int(b)
    if a==0 or b==0:
        print("Введите другие значаения для а и b!!!")
    else:
        fig, ax = plt.subplots()
        x=np.linspace(-10,10,1000)
        y=3+(2/(a*x))+3/(b*x**2)
        ax.plot(x,y)
        plt.show()

except ValueError:
    print("Введите другое значаение для n!!!")

