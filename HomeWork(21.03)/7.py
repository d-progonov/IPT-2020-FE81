x = input("Введіть двозначне число: ")
if int(x) >= 10 and int(x) <= 99:
    if int(x[0]) > int(x[1]):
        print("Більше число: ", x[0], "\nМенше число: ", x[1])
    elif int(x[0]) < int(x[1]):
        print("Більше число: ", x[1], "\nМенше число: ", x[0])
    else: print("Числа одинакові")
else: print("error")
