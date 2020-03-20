Sum = 0
if __name__ == '__main__':

    while True:
        try:
            while True:
                n = int(input("Enter number: "))
                if n % 3 != 0 and n % 2 != 0 and n > 0:
                    print("")
                    break
        except ValueError:
            print("Invalid value")
        else:
            break

    for i in range(1, n+1):
        var = (i ** 3 - 3 * i * n ** 2 + n)
        if var % 3 == 0 and var % 2 != 0:
            Sum += var
        # print(var)
    print("Sum = ", Sum)
