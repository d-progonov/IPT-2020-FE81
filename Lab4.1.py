import random
n = int(input("Enter size of array: "))
a = 2 * n
c = 2
temp = 0
array = []
arrayT = []
for i in range(a):
    array.append([])
    for j in range(a):
        array[i].append(random.randint(0,10))

for i in range(a):
    arrayT.append([])
    for j in range(a):
        arrayT[i].append(0)

print(array)

for i in range(a):
    arrayT.append([])
    for j in range(a):
        arrayT[i][j] = array[j][i]

print(arrayT)
