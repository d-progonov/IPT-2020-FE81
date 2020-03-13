while(1):
    try:
        s = float (input("Enter s = "))
        break
    except Exception:
        print("Wrong data type for variable s (must be float).")
while(1):
    try:
        t = float (input("Enter t = "))
        break
    except Exception:
        print("Wrong data type for variable t (must be float).")

def h(a, b):
    return a/(1+b**2)+b/(1+a**2)-(a-b)**3

print("h:=a/(1+b^2)+b/(1+a^2)-(a-b)^3")
print("h(s,t)+max(h^2(s-t,st),h^4(s-t,s+t))+h(1,1)")
print("Result ={:0.2f}".format(h(s,t)+max((h(s-t,s*t))**2,(h(s-t,s+t))**4)+h(1,1)))
input("Any key to exit...")