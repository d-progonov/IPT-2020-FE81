try:
    n = int(input("Enter n:"))
    print("Your tripled and odd numbers :")
    for i in range(1, n, 1):
        if (i/3) % 2 == 1:
            print(str(i))
except ValueError:
    print("ERROR you should enter a number but not string!!!")