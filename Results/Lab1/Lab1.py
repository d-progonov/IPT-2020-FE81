g = True
x = input("input x: ")
z = input("input z: ")

def is_digit(t):
    if t.isdigit():
       return True
    else:        
        try:
            float(t)
            return True
        except ValueError:
            print(t,"not a number")
            return False

if is_digit(x) and is_digit(z):
    x = float(x)
    z = float(z)
    while g:
        k = x**2/4
        if k == z:
            print("wrong answer, please enter another values")
            x = float(input("input x: "))
            z = float(input("input z: "))
            k = x**2/4
        else:
            y = x - z/(z-k)-x**2/120
            print(y)
            g = False
else:
    print("Please use numbers")
