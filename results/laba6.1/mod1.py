import math
def P(x,y):
    P=0
    for i in range(10):
        length=math.sqrt((x[9-i]-x[9-i-1])**2+(y[9-i]-y[9-i-1])**2)
        P=P+length

    print("Периметр:",P)