import math
x=input("Enter x:")
c=input("Enter c:")
b=input("Enter b:")
try:
    x = float(x)
    c = float(c)
    b=float(b)
    if((x-b)>0):
        y=((2*x-c)/(math.sqrt(x-b))+abs(x-c))
        print(y)
    else:
        print("ЭЭЭЭЭ это ты что удумал , что это за данные что это за данные вчера же всё нормально было а ну давай всё поновой")
except ValueError:print("Введите норальные значения!!!")