def func():
    try:
        a=int(input("Введите значение а: ")) 
        b=int(input("Введите значение b: "))
        f=int(input("Введите значение f: "))
        y=(a + b - f / a) + f * a * a - (a + b)
        print(y)
    except ValueError:
        print("Неправильные данные")
    except ZeroDivisionError:
        print("Ошибка деления на 0")
func()        