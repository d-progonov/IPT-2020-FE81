def func():
    try:
        a=int(input("Введите значение а: ")) 
        b=int(input("Введите значение b: "))
        f=int(input("Введите значение f: "))
        if(a==b or a==f or b==f):
            print(a+5)
            print(b+5)
            print(f+5)
        else:
            print("Равных нет")            

    except ValueError:
        print("Неправильные данные")  
func()        