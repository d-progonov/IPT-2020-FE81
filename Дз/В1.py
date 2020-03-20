def func():
    try:
        n=int(input("Введите пятизначное число: "))
        if (n>99999):
            print("Error")
        elif (n<9999):
            print("Error")
          
        i=10000
        while(i>=1):
            print(int(((n//i)%10)))
            i/=10

    except ValueError:
        print("Неправильные данные")
func()