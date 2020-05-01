import math

n=int(input("Кол-во элем: ")) 
sum = 0
for i in range(1,n+1):
    a = math.sqrt(i)    
    if (float.is_integer(a)):         
        sum = sum + a
        print(i)     
    else:
        print("Число не целое!")
print(sum)


