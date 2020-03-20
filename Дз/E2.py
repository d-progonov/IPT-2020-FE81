def func():
    try:
        n=abs(int(input("Введите двухзначное число: ")))
        if (n>99):
            print("Error")
        elif (n<9):
            print("Error")
        else:
            print("Минимально число: ",min(list(str(n))))
            print("Максимальное число: ",max(list(str(n))))
    except ValueError:
        print("Неправильные данные")
func()