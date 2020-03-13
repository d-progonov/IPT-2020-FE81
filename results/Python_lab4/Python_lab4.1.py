import random
while(1):
    try:
        n = int (input("Enter n = "))
        1/(n+abs(n))
        break
    except Exception:
        print("Wrong data type for variable n (must be natural int).")

items = [random.randint(10, 99) for i in range(n)]
print("List:", items)

items2 = []
itemstemp = []

for i in range(n):
    itemstemp.clear()
    j = 0
    while j<n:
        itemstemp.append(items[i])
        j+=1
        if j>=n:
            break
        itemstemp.append(items[n-1-i])
        j+=1
    items2.append(itemstemp.copy())

print("Matrix:")
for i in range(n):
    print(items2[i])
input("Any key to exit...")