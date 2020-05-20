import numpy as np
import matplotlib.pyplot as plt 
import pylab

x_list = list()
y_list = list()

while True:
    try:
        l_bound_x = int(input("Введите левую границу 'x':"))
        break
    except ValueError:
        print("Введите целое число!")

while True:
    try:
        r_bound_x = int(input("Введите правую границу 'x':"))
        if r_bound_x < l_bound_x:
            print("Правая граница не может быть больше левой, введите правильное число:")
            continue
        break
    except ValueError:
        print("Введите целое число!")
        

while True:
    try:
        l_bound_y = int(input("Введите нижнюю границу 'y':"))
        break
    except ValueError:
        print(" Введите целое число!")

while True:
    try:
        r_bound_y = int(input("Введите верхнюю границу 'y':"))
        if r_bound_y < l_bound_y:
            print("Верхняя граница не может быть ниже нижней, введите правильно число:")
            continue
        break
    except ValueError:
        print("Введите целое число!")
        
if __name__ == '__main__':
    for x in np.arange(l_bound_x, r_bound_x , 0.05):
        for y in np.arange(l_bound_y, r_bound_y , 0.05):
            if  x * x + y * y >=1 *(abs(x) + abs(y)) and x * x + y * y <= 4 :
                x_list.append(x)
                y_list.append(y)
                print("Множество точек:", '(', x, ',', y, ')')
                
    if len(x_list) == len(y_list) == 0:
        print("В графике нет точек!")

    pylab.xlim(l_bound_x, r_bound_x)
    pylab.ylim(l_bound_y, r_bound_y)
    pylab.grid()
    plt.scatter(x_list, y_list, alpha=0.1)
    plt.title('Лабораторная работа 8')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
