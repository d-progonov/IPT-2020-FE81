import math
def check(NUM,POINT):
    check_help=True
    try:
        num=float(NUM)
    except ValueError:
        print("Error; A must be integer either a float")
        check_help=False
    try:
        point=float(POINT)
    except Va2lueError:
        print("Error; B must be integer either a float")
        check_help=False
    return check_help
def lab1():
    while 1:
        a=input("A= ")
        b=input("B= ")
        if check(a,b)== False:
            continue
        else:
            a=float(a)
            b=float(b)
            break
    try:
        y=(a-2)/(2*a+b)+(math.sin(3*a)/math.cos(b))
        print("COMPLETED SUCCESSFULLY.".format(y))
    except ZeroDivisionError:
        print("Error; Divided by zero")
lab1()