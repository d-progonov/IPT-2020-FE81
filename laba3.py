import math
s=0
#n=input("Enter n:")
n=0
try:
    n=int(n)
    while(((3**n)*math.factorial(n))/(math.factorial(3*n))>10**-4):
        s=s+((3**n)*math.factorial(n))/(math.factorial(3*n))
        n+=1
    print(s)
except ValueError:print("Введите другое значаение для n!!!")