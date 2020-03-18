from random import randint
while(1):
    try:
        n = int (input("Enter n: "))
        if n<1:
            raise ValueError
    except ValueError:
        print("Wrong data type for variable n (must be natural int).")
        continue
    break

a = [randint(-99, 99) for i in range(n)]
a2 = []
for elem in a:
    if elem%2==0:
        a2.append(elem)
print("Original array:\n", a)
print("Only a = 2k:\n", a2)
