try:
    x=int(input("Введите число:"))
    res=abs(x)
    print("Абсолютное значение числа:", res)

except ValueError:
        print("Неправильные данные")