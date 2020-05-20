class Exception(Exception):
    def init(self, text):
        self.txt = text

def check_perfect_square(a):
    if (a == 1):
        print("Processing Error!")
        raise Exception("The 'a' must not equal to 1!")

    x = a // 2                   
                                 
    seen = set([x])              
    while x * x != a:            
        x = (x + (a // x)) // 2  
        if x in seen:             
            return False    
        seen.add(x)              
                                 
    return True


def f(n, a, c):
    
    def g(n):    
        res = (a*n + a*c) % 10
        return res

    if (0 <= n <= 9):
        return n
    
    else:
        res = g(n) * f((n-1-g(n)), a, c) + n
        return res