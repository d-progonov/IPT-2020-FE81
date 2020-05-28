import math
    
def lab2 ():
    while 1:
        try:
            count=int(input("Specify total amount of loaded degree rate: "))
        except ValueError:
            print("degree rate must be integer.")
            continue
        if count<=0:
            print("degree rate must be positive.")
            continue
        for x in range(1,count+1):
            print("{}. Set number to {} degree;".format(x,x+1))
        try:
            num=float(input("Please enter the number: "))
        except ValueError:
            print("Error. Enter float or integer number")
            continue
        if math.isnan(num):
            print("Error, try again")
            continue
        if math.isinf(num):
            print("Number can not be an infinity")
            continue
        try:    
            point=int(input("Please choose the dimension rate: "))
        except ValueError:
             print("Error.Enter integer in [1:{}]".format(count))
             continue
        if point<=0 or point>count:
            print("Error, choose coorect punct")
        print("Result is: {0}".format(num**(point+1)))
        break

if __name__ == "__main__":
    lab2()
