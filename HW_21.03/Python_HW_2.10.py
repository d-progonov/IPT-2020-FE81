print("y=ax^2+bx+c   y=dx+k")
while(1):
    try:
        a = float (input("Enter a = "))
        break
    except Exception:
        print("Wrong data type for variable a (must be float).")
while(1):
    try:
        b = float (input("Enter b = "))
        break
    except Exception:
        print("Wrong data type for variable b (must be float).")
while(1):
    try:
        c = float (input("Enter c = "))
        break
    except Exception:
        print("Wrong data type for variable c (must be float).")
while(1):
    try:
        d = float (input("Enter d = "))
        break
    except Exception:
        print("Wrong data type for variable d (must be float).")
while(1):
    try:
        k = float (input("Enter k = "))
        break
    except Exception:
        print("Wrong data type for variable k (must be float).")

# ax^2+x(b-d)+(c-k)=0

dis = pow(b-d,2)-4*a*(c-k)
if dis<0:
    print("No")
elif dis == 0:
    x0 = (d-b)/(2*a)
    print("1) ({}, {})".format(x0, d*x0+k))
else:
    x1 = ((d-b)+pow(dis,0.5))/(2*a)
    x2 = ((d-b)-pow(dis,0.5))/(2*a)
    print("1) ({}, {})".format(x1, d*x1+k))
    print("2) ({}, {})".format(x2, d*x2+k))
input("Any key to exit...")