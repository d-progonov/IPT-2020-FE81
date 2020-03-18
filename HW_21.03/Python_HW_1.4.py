while(1):
    try:
        a = float (input("Enter a = "))
        break
    except ValueError:
        print("Wrong data type for variable a (must be float).")
while(1):
    try:
        b = float (input("Enter b = "))
        break
    except ValueError:
        print("Wrong data type for variable b (must be float).")

if a>b:
    print("больше")
if a<b:
    print("меньше")
else:
    print("Эти числа равны")
input("Any key to exit...")