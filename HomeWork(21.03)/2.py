a = input("Enter a: ")
b = input("Enter b: ")
f = input ("Enter f: ")
a = int(a)
b = int(b)
f = int(f)
if a == 0:
    print("Error, enter anther values")
else:
    ans = (a+b-f/a)+f*a*a-(a+b)
    print("Answer: ",ans)
