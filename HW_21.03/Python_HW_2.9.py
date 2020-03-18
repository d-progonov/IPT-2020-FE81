while(1):
    try:
        n = int (input("Enter n = "))
        if n<0:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for variable n (must be positive int).")
s = 0
i = 0

#while(i<=n):
#    if i%5 == 0:
#        s+=i
#    i+=1

while(i<=n):
    s+=i
    i+=5

print("Result:", s)
input("Any key to exit...")
