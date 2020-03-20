try:
    first = float(input("Введите первое число "))
    second = float(input("Введите второе число "))
    if first > second:
        print("Больше")
    elif first < second:
        print("Меньше")
    else:
        print("Эти числа равны")
except ValueError:
    print("ERROR you should enter a number but not string!!!")