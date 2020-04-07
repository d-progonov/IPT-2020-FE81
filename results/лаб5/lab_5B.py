import math

def if_nan():
    print("Error! Not a number!")

def fast_exp(b, n):
    def even(n):
        if n % 2 == 0:
            return 1
        return 0
    if n == 0:
        return 1
    if even(n):
        return fast_exp(b, n / 2) ** 2
    return b * fast_exp(b, n - 1)

while True:
    try:
        B = input("Input any rational number, please:")
        if B == "pi":
            b = math.pi
            break
        elif B == "e":
            b = math.e
            break
        elif B == "inf":
            b = float('inf')
        elif B == "nan":
            if_nan()
            continue
        b = float(B)
        break
    except valueError:
        print("Invalid value entered!")

while True:
    try:
        n = float(input("Input value‘s positive integer power:"))
        if not n > 0 or n % 1 != 0:
            print("Error! value‘s power has to be positive and integer. Please, input the proper one:")
            continue
        break
    except ValueError:
        print("Invalid value enteredt")

if __name__ == '__main__':
    print(fast_exp(b, n))
