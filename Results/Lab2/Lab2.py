x = input("Input your number: ")
k = True
i = True
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

if is_digit(x):
    x = float(x)
    print("Press 2 if you want to get a square of that number, 3 to get a cube:")
    while(k):
        print("(%s)"%(x),end="^")
        oper = input()
        if is_digit(oper):
            oper = float(oper)
            if oper == 2:
                x = x**2
                print("Answer: ", x)
            elif oper == 3:
                x = x**3
                print("Answer: ", x)
            else:
                print("Please enter 2 or 3")
            print("Do you want to continue?")
            i = True
            while(i):
                ans = input("(y/n):\t")
                if ans == "y":
                    k = True
                    i = False
                elif ans == "n":
                    k = False
                    i = False
                else:
                    print("Write yes or no")
        else:
            print("Error. Check that the number is entered correctly (You enter: %s)" %(oper))
else:
    print("Please use numbers")
