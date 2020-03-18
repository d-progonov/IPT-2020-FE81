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
while(1):
    try:
        c = float (input("Enter c = "))
        break
    except ValueError:
        print("Wrong data type for variable c (must be float).")

if (a==b or b==c or a==c):
    a+=5
    b+=5
    c+=5
print("a = {}, b = {}, c = {}.".format(a,b,c))
input("Any key to exit...")