class NumberError(Exception):
    pass

while (True):
    try:
        x=abs(int(input("Enter x=")))
        if 10000> x <99999:
            raise NumberError
        break
    except ValueError:
        print("Wrong data type of x")
    except NumberError:
        print("Must consist of 5 digits ")

i=10000
while(i>=1):
    print(int(((x//i)%10)))
    i/=10
    