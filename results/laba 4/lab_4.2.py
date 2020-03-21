import random
import numpy

while (1):
    try:
        n = int(input("Enter n = "))
        break
    except Exception:
        print("Error, enter int number ")

arr = [random.randint(0, 100) for i in range(n)]
print("List:    ", arr)

min_value = min(arr)
print(min_value)

for i in range(-len(arr), 1):
    if (arr[i] == min_value):
        del arr[i]
print("No element with minimal value:   ", arr)

average_value = numpy.mean(arr)
for i in range(0, 3, 1):
    arr.insert(0, average_value)

print("Add 3 element average_value:  ", arr)
