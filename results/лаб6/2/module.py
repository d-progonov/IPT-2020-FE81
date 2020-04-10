import math

def read():
    try:
        file = open('reading.txt', 'r')
    except FileNotFoundError:
        print("File is not found! Check whether it is in the same directory with your project")
        exit()

    inp = [line.strip() for line in file]
    file.close()
    return inp

def write(part):
    file = open('writing.txt', 'w')
    file.write(part)
    file.close()
    return True

def fast(b, n):
    def even(n):
        if n % 2 == 0:
            return 1
        return 0
    
    if n == 0:
        return 1
    if even(n):
        return fast(b, n / 2) ** 2
    return b * fast(b, n - 1)


def value(inpVal):
    try:
        my_value = inpVal
        if my_value == 0:
            print("Iour value can‘t be '0'! Choose another value, please")
        elif my_value == "pi":
            my_value = math.pi
            return my_value
        elif my_value == "inf":
            my_value = float('inf')
            return my_value
        elif my_value == "e":
            my_value = math.e
            return my_value
        elif my_value == "nan":
            print("Invalid value! Can t be not a number!")
            return False
    except ValueError:

        print("Invalid value entered! Input another one, please!")
        return False
    else:
        my_value = float(inpVal)
        return my_value

def power(inpPow):
    try:
        my_power = int(inpPow)
        if my_power <= 0:
            print("The power of your value must be positive and integer! Choose another one, please")
            exit(0)
    except ValueError:
        print("Invalid value! The power of your value must be positive and integer!")
        return False
    else:
        return my_power
