import math
def func():
    try:
        x=float(input("Введите значение x: "))
        y=float(input("Введите значение y: "))
        a=(1-math.tan(x))**(1/math.tan(x))+math.cos(x-y)
        print(a)
    except ValueError:
        print("Неправильные данные")  
func()        