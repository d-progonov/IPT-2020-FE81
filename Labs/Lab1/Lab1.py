import math
def function():
    try:
        x = int(input("Первое число:"))                
        z = int(input("Второе число: "))
        y = math.sqrt(abs((x**2)-4))/(2*z)
        print("Результат:", y)
    except ValueError:
        print("Неправильные данные")
    except ZeroDivisionError:
        print("Ошибка деления на 0")  
function()









