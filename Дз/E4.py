import math  

def func():
    try: 
        x = int(input("x= "))
        y = int(input("y= "))
        z = int(input("z= "))
        l=math.sqrt(x*x+y*y+z*z)
        print("Длина вектора: ", l)
    except ValueError:
        print("Неправильные данные")  
func()        