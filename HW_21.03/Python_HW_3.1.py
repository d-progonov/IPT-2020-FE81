while(1):
    try:
        n = int (input("Enter n = "))
        if n<0:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for variable n (must be positive int).")

def recurs(iter):
    if iter==0:
        return 1;
    else:
        return (1+1/recurs(iter-1))

print("Result:", recurs(n))
input("Any key to exit...")
