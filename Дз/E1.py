def func():
    try:
        N=int(input("Kolvo el: "))
        k=int(input("Stepin: "))
        sum=0
        for i in range (1, N+1):
            sum+=i**k
        print(sum)
    except ValueError:
        print("Неправильные данные")  
func()        