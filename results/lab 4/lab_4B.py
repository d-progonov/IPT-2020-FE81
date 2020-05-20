import random

N = int(input("Enter N: "))
array = []

for i in range(0, N):
    array.append(random.randint(0, 10))

print("Our array: ", array)

array = array[:-5]
print("Our array, without 5 last elements: ", array)

for I in range(0, 3):
    print("array[I + 1]: ", array[I + 1] + 2)
    C = array[I + 1] + 2
    array.insert(0, C)

print("Our array with 3 new elemengts: ", array)