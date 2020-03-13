while(1):
    try:
        n = int (input("Enter n = "))
        1/(n+abs(n))
        break
    except Exception:
        print("Wrong data type for variable a (must be natural int).")
for i in range(n):
    b = str((i+1)**2)
    a = str(i+1)
    yes = True
    for j in range(len(a)):
        if b[len(b)-1-j]!=a[len(a)-1-j]:
            yes = False
            break
        if j+1==len(a):
            print("{} and {}".format(a, b))
input("Any key to exit...")
