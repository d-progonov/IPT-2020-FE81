try:
    a = float(input("Enter your first number"))
    b = float(input("Enter your second number"))
    c = float(input("Enter your third number"))
    if (a==b or a==c or b==c):
        a+=5
        b+=5
        c+=5
        print(a, ",", b, ",", c)
    else:
        print("равных нет")
except ValueError:
    print("ERROR you should enter a number but not string!!!")