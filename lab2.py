import math
x=input("Enter x:")

try:
    x = float(x)

    if(x>=0):
        print("знак числа:+")
    else:
        print("знак числа:-")
except ValueError:print("Введите норальные значения!!!")