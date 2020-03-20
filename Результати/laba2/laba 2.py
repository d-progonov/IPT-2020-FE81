import math

x = 18 % 8

while True:
    try:
        A = input("a = ")
        if A == "inf":
            print("Arg 'a' is Infinity")
            a = math.inf
            break
        elif A == "nan":
            print("Not a number! Input a value, please:")
            continue
        a = float(A)
        break
    except ValueError:
        print("Invalid value entered!")
while True:
    try:
        B = input("b = ")
        if B == "inf":
            print("Arg 'b' is Infinity")
            b = math.inf
            break
        elif B == "nan":
            print("Not a number! Input a value, please:")
            continue
        b = float(B)
        break
    except ValueError:
        print("Invalid value entered!")

if __name__ == '__main__':
    print("Task number:", x)

    if a == math.inf and not b == math.inf:
        print("Answer: Infinity is max, value b =", b, "is min")
    elif b == math.inf and not a == math.inf:
        print("Answer: Infinity is max, value a =", a, "is min")
    elif a == b and not a and b == math.inf:
        print("Args 'a' and 'b' are equal")
    elif a and b == math.inf:
        print("Impossible to compare infinities!")
    elif a - b > 0:
        print("Value 'a' =", a, "is max", "value 'b' =", b, "is min")
    else:
        print("Value 'b' =", b, "is max", "value 'a' =", a, "is min")
