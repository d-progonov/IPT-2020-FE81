import random
import math

def P(x,y):
    P=0
    for i in range(10):
        length=math.sqrt((x[9-i]-x[9-i-1])**2+(y[9-i]-y[9-i-1])**2)
        P=P+length

    print("Периметр:",P)


x=[]
y=[]
try:
    for i in range(10):
        x.append(random.randint(1,100))
        y.append(random.randint(1, 100))
    print("x:",x)
    print("y:",y)
    P(x,y)

except ValueError:print("Что то пошло не так как надо!!")