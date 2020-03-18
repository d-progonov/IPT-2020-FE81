from math import sin

while(1):
    try:
        n = int (input("Enter n = "))
        if n<1:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for variable n (must be positive int).")

s = 0;
for i in range(1, n+1):
    temp = 0
    for j in range(1, i+1):
        temp+=1/sin(j)
    s+=temp

print("S =",s)
input("Any key to exit...")