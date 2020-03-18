class Error(Exception):
    pass

while(1):
    try:
        s = int (input("Enter string = "))
        break
    except ValueError:
        print("Wrong data type for string (must consist of numbers).")
while(1):
    try:
        i = int (input("Enter index = "))
        if i<1:
            raise ValueError
        if i>len(str(s)):
            raise Error
        break
    except ValueError:
        print("Wrong data type for string (must be natural int).")
    except Error:
        print("Position is too far? No such position in given string.")

s = str(s)
print("The number in string in position {} is {}.".format(i,s[i-1]))
input("Any key to exit...")