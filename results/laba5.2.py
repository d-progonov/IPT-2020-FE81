def func(x,n):
    return x**n

x=input("Enter x:")
n=input("Enter n:")

try:
    n=int(n)
    x=float(x)
    if n>0 and x!=0 :
        print(func(x,n))


except ValueError:print("Введите другое значаение для n!!!")