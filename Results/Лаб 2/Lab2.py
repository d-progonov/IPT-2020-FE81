import math

What=input("Введите что будем решать (cos,sin,tan)")

a=float(input("теперь введите ваше число которое хотите обчислить"))

if What=="cos":
    b=math.cosh(a)
    print("Результат:",b)
elif What=="sin":
    b=math.sinh(a)
    print("Результат:",b)
elif What=="tan":
    b=math.tanh(a)
    print("Результат:",b)

    
    
           
