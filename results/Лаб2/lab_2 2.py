import math
while True:
    try:
        X = input("x = ")
        x = float(X)
        if isinstance(x, float) and (not math.isnan(x)):
            print()
            break
    except ValueError:
            print("Is not a number! Try again!")

while True:
    try:
        Y = input("y = ")
        y = float(Y)
        if isinstance(y, float) and (not math.isnan(y)):
            print()
            break
    except ValueError:
        print("Is not a number! Try again!")

A = math.inf
if x == A and y == A:
    print("невозможно вычислить")
elif x == -A and y == -A:
    print("невозможно вычислить")
elif x > y:
    print("min:", y)
else:
    print("min:", x)
    from time import sleep
    sleep(1e3)
