import math

try:
    x = float(input("Введите значение переменной x: "))
    if (x >= math.sqrt(5) or x <= -(math.sqrt(5))):
        y = float(math.sqrt(math.log((x**2)-4)))
        print("Ваш ответ: ", y)
    else:
        print("Некорректное значение переменной x !")

except :
        print("Проверьте Ваши данные и введите заново!")
