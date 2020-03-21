import math

try:
    x = float(input("Enter x : "))
    z = float(input("Enter z : "))
    if z != 2 :
        y = x*math.atan(z)+math.e**-((x+3)/(z-2))
        print("Ваш ответ :", y)
    else:
        print("Неверное значение переменной z\n")
except ValueError:
    print("Было введено неверное значение")

