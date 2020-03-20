def func():
    try:
        a=int(input("Введите число: ")) 
        n=int(input("Степень этого числа: "))
        y=1
        for i in range (1, n+1):
            y*=a
            i=i+1
        print(y)
    except ValueError:
        print("Неправильные данные")
func()