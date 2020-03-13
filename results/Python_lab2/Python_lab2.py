
while(1):
    try:
        x = float (input("Enter x = "))
        break
    except ValueError:
        print("Wrong data type for variable x (must be float).")
if (x<0):
    x*=-1
print("Absolute value of x = ", x)
input("Any key to exit...")