while(1):
    try:
        a =int (input("Enter a = "))
        if a < 1:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for variable a (must be natural int).")
while(1):
    try:
        b =int (input("Enter b = "))
        if b < 1:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for variable b (must be natural int).")
while(1):
    try:
        c =int (input("Enter c = "))
        if c < 1:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for variable c (must be natural int).")
while(1):
    try:
        d =int (input("Enter d = "))
        if d < 1:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for variable d (must be natural int).")

for x in range(1, d//a):
    for y in range(1, d//b):
        for z in range(1, d//c):
            if x*a + y*b + z*c == d:
                print('Point({0},{1},{2})   x = {0}; y = {1}; z ={2}.'.format(x,y,z))