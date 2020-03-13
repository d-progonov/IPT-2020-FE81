a = input('a = ')

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        a = input("Please, enter a number. a = ")

b = input('x = ')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        b = input("Please, enter a number. b = ")

print('min =', min(a,b))