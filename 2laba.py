import math

while True:
    a = input("Введите число a: ")
    try:
        a1 = float(a)
        if math.isnan(a1):
            print("Невозможно выполнить действия с не числом (NaN). Введите число.")
            continue
        print('Число а = ', a1)
        break
    except (TypeError, ValueError):
        print('Это не число')

while True:
    b = input("Введите число b: ")
    try:
        b1 = float(b)
        if math.isnan(b1):
            print("Невозможно выполнить действия с не числом (NaN). Введите число.")
            continue
        print('Число b = ', b1)
        break
    except (TypeError, ValueError):
        print('Это не число')


if a1 < b1:
    print(a1, "- минимальное")
elif a1 == math.inf and b1 == math.inf:
    print("Невозможно определить")
elif a1 == -math.inf and b1 == -math.inf:
    print("Невозможно определить")
elif a1 == b1:
    print("Числа равны")
else:
    print(b1, "- минимальное")