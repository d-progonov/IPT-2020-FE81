import random
from mod1 import P

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