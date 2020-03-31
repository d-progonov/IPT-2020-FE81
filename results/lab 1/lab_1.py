import math

try:
    x = float(input("Введите значение переменной x: "))
    if math.fabs(x) > 2:
        y = float(math.sqrt(math.log((x**2)-4)))
        print("Ваш ответ: ", y)
    else:
        print("Некорректное значение переменной x!")

except ValueError:
        print("Проверьте Ваши данные и введите заново!")
