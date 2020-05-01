from math import sqrt
def func(N):
    
    sum = 0
    for i in range(1,N+1):
        a = sqrt(i)    
        if (float.is_integer(a)):         
            sum = sum + a     
        else:
            print("Число не целое!")
    return sum
    

def ncd(n, m):
    if m == 0: 
        return n
    else: 
        return ncd(m, n % m) 
     

