while(1):
    try:
        x = float (input("Enter x = "))
        break
    except ValueError:
        print("Wrong data type for coordinate x (must be float).")
while(1):
    try:
        y = float (input("Enter y = "))
        break
    except ValueError:
        print("Wrong data type for coordinate y (must be float).")
while(1):
    try:
        z = float (input("Enter z = "))
        break
    except ValueError:
        print("Wrong data type for coordinate z (must be float).")

l = pow((pow(x,2)+pow(y,2)+pow(z,2)),0.5)
print("a = ({}; {}; {})".format(x, y, z))
print("|a| = ", l)
input("Any key to exit...")