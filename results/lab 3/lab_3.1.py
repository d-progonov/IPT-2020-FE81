import math

try:
    total = 0
    n = 0
    while True:
        pip = pow(math.factorial(n),2)/pow(2,(n**2))
        print("a(n)({0})={1}".format(n,pip))
        if pip <= pow(10,-4):
            break
        total += pip
        n = n+1
        

    print("Sum of this row is: ", round(total, 4))

except:
    print("Error! Chek data you entered!")

