
import random
while(1):
    try:
        n = int (input("Enter n = "))
        break
    except Exception:
        print("Wrong data type for variable n (must be int).")

items = [random.randint(-99, 99) for i in range(n)]
print("List:  ", items)

for i in range(-len(items), 1):
    if (i%3)==0:
        del items[abs(i)]
print("No %3: ", items)
i = 0
for item in items:
    if item<0:
        if i == 0:
            items.insert(i+1, 0)
        else:
            items.insert(i+1, abs(items[i-1]+1))
    i+=1
print("Result:", items)
input("Any key to exit...")
