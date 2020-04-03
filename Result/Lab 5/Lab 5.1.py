
try:
    u1 = float(input("Enter u1 : "))
    u2 = float(input("Enter u2 : "))
    v1 = float(input("Enter v1 : "))
    v2 = float(input("Enter v2 : "))
    w1 = float(input("Enter w1 : "))
    w2 = float(input("Enter w2 : "))
    u = complex(u1,u2)
    v = complex(v1,v2)
    w = complex(w1,w2)
    def func(u,v,w):
        return ((2*u)+(((3*u)*w)/((2+w)-u))-(7*v))
        
    print(func(u,v,w))
except ValueError:
    print("You entered the wrong type")
