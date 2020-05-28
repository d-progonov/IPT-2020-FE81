from math import isnan, isinf

available_six = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']

def bin_to_dec(inp):
    return int(inp, 2)

def six_to_dec(inp):
    return int(inp, 16)

def check_bin(inp):
    for i in range(len(inp)):
        if not inp[i] == '1' and not inp[i] == '0':
            print("There are not just 0 or 1")
            return False
    return True

def check_six(inp):
    for i in range(len(inp)):
        if not inp[i] in available_six:
            print("There are errors numbers")
            return False
    return True

if __name__ == "__main__":

    while True:
        print("Choose a system(10 - Decimal, 2 - Binary, 16 - Hexadecimal) ")
        system = input('-> ')

        if not system == '10' and not system == '2' and not system == '16':
            print("There are not this system")
            continue
        else: break

    inp_num = input("Enter a number: ")
    if system == '2':
        if not check_bin(inp_num):
            print("Exit")
            exit()
        else:
            print("Your number in decimal: {}".format(bin_to_dec(inp_num)))

    elif system == '10':
        try:
            inp_num = float(inp_num)
        except ValueError:
            print("It must be a nuber.")
            exit()
        if isnan(inp_num):
            print("Its not a number.")
            exit()
        elif isinf(inp_num):
            print("This is infinity.")
            exit()
        elif not inp_num.is_integer():
            print("The number is not integer")
            exit()
        else:
            inp_num = int(inp_num)
            print("Yout number is: {}".format(inp_num))

    elif system == '16':
        if not check_six(inp_num):
            print("Exit.")
            exit()
        else:
            print("Your number is: {}".format(six_to_dec(inp_num)))
