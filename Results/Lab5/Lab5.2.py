def is_digit(temp):
    if temp.isdigit():
       return True
    else:        
        try:
            int(temp)
            return True
        except ValueError:
            print(temp,"не ціле число")
            return False
n = input("Введіть n і m для функції A(n,m):\nn = ")
m = input("m = ")

def A(n0,m0):
    n = n0
    m = m0
    if n0 == 0:
        return m0+1
    elif n0 != 0 and m0 == 0:
        m = A(n0-1,1)        
        return m
    else:
        res = A(n0,m0-1)
        m = A(n0-1,res)        
        return m
try:
    n = int(n)
    m = int(m)
    if n >= 0 and m >= 0:
        m = A(n,m)
        print("Відповідь: ", m)    
except ValueError:
    print("Введіть невід'ємні числа")
