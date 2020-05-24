

import math
s=10**(-4)
n=1
a=0
while(10**n)/(math.factorial(n))>s:
     a+=(10**n)/math.factorial(n)
     n+=1
     print(round(a,4))
print("Просумирование равно:",round(a,4))
 
