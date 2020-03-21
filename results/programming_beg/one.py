def func():
    try:
        n=int(input("Введите 5тизначное число: "))
        if n < 10000 and n > 99999:
            print('Ошибочка')
          
        i=10000
        while(i>=1):
            print(int//10000, int//1000%10, int//100%10, int//10%10, int%10)
            i/=10

    except ValueError:
        print("Может попробуешь с 5тизначным числом?")
func()
