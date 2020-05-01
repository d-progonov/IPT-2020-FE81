import random
temp=[]
n = int(input("Enter n: "))
arr = [random.randint(0, 100) for i in range(n)]
print("Array before :", arr)
arr.reverse()
print("Reversed array :", arr)
if n % 2 != 0:
    middle= (n//2)
    del arr[middle]
    print("Array without middle element :", arr)
else:
    print("Array have not middle element!")
if n >= 14:
    for j in range (0, 3):
        temp.insert(j,arr[j+10]-2)
    for i in range(0, 3):
        arr.insert(i, temp[i])
else:
    print("We can`t do this transformation, because 'Out of range ERROR!!!' ")
print("Final array :", arr)





