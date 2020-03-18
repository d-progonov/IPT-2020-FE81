while(1):
    try:
        a = float (input("Enter a = "))
        break
    except ValueError:
        print("Wrong data type for variable a (must be float).")
while(1):
    try:
        n = int (input("Enter n = "))
        if n<0:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for variable n (must be positive int).")

res = 1
print("{}^{} = ".format(a, n), end='')
while (n != 0):
    res*=a
    n-=1
print(res)
input("Any key to exit...")