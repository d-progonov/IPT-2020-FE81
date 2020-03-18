while(1):
    try:
        N = int (input("Enter N = "))
        if N<10 or N>99:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for variable N (must be two-digit natural int).")

first = int((N-N%10)/10)
second = int(N%10)

if first > second:
    print("Max: {0}\nMin: {1}".format(first, second))
else:
    print("Max: {1}\nMin: {0}".format(first, second))
input("Any key to exit...")
