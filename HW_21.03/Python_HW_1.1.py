while(1):
    try:
        a = abs(int(input("Enter a = ")))
        if (a<10000 or a>99999):
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for variable a (must be five-digit int).")

i = 10000

while (i>=1):
    print(int(((a-a%i)/i)%10))
    i/=10
input("Any key to exit...")