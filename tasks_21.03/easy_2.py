class NumberError(Exception):
    pass
while (True):
    try:
        N=int(input("Enter N ="))
        if N<1:
            raise ValueError
        if 10< N >99:
            raise NumberError
        break
    except ValueError:
        print("Wrong data type of N(must be natural number)")
    except NumberError:
        print("Number must consist of 2 digits")
a=N//10
b=N%10
if a>b:
    print("Max={0}, min={1}".format(a,b))
elif a<b:
    print("Max={0}, min={1}".format(b,a))
else:
    print("Numerals are equal")