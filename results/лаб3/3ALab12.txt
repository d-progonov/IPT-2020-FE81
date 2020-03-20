import math
Sum = 0
n = 2

if __name__ == '__main__':

    while True:
        try:
            eps = float(input("Enter accuracy: "))
        except ValueError:
            print("Invalid value")
        else:
            break

    while True:
        temp = math.log10(math.factorial(n)) * math.exp(math.sqrt(n) * (-n))
        Sum += temp
        print(Sum)
        if temp < math.fabs(eps):
            break
        n = n+1

    print("Sum of series =", Sum)

