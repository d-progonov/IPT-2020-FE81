a = input('A = ')
while type(a) != float:
    try:
        a = float(a)
        break
    except ValueError:
        a = input("Enter a number. A = ")

b = input('B = ')
while type(b) != float:
    try:
        b = float(b)
        break
    except ValueError:
        b = input("Enter a number. B = ")

c = input('C = ')
while type(c) != float:
    try:
        c = float(c)
        break
    except ValueError:
        c = input("Enter a number. C = ")

print('Minimal number is ', min(a,b,c))
