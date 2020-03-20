def func():
    try:
        a=int(input("Введите первое число: "))
        b=int(input("Введите второе число: "))
        if(a>b):
            print("больше")
        elif(a<b):
            print("меньше")
        elif(a==b):
            print("числа равны")    
    except ValueError:
        print("Неправильные данные")            
func()        