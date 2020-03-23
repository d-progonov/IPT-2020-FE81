import random
from statistics import mean

n=int(input("Кол-во элементов: "))
arr=[]

for i in range (0,n):
    a=random.randint(1,n)
    arr.append(a)
print(arr)   

maximum = max(arr)
minimum = min(arr)

for i in range(len(arr)):
  if (arr[i] == maximum):
    arr[i] = minimum
    
  elif (arr[i] == minimum):
    arr[i] = maximum
print(arr)    

 
x=mean(arr)
y=x - (x / 100 * 10) # Average+10%
print(y)
i = 0
while i < len(arr):
	if arr[i] > y:
		del arr[i]
	else:
		i += 1  
print (arr)  





