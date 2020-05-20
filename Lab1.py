import math

def calc(x,b):
    if b == 0 or x - b < 0:
        return math.inf
    return (math.sqrt(x-b))/(2*b) - math.tan(x)/pow(b,2)

def getValue():
    try:
        x = int(input("Enter x = "))
        b = int(input("Enter b = "))
        return calc(x,b)
    except ValueError:
        print("Wrong value")

def main():
    print("Looking for some values)\n Enter 2 numbers\n")
    while True:
            result = getValue()
            print(result)


if __name__ == "__main__":
    main()
