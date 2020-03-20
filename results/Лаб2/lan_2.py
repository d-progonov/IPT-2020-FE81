import math

while True:
    try:
        number = float(input("Enter number: "))
    except ValueError:
        print("Invalid value")
    else:
        break

print(math.fabs(number))
