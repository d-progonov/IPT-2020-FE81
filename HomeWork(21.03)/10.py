import math
x = input("Enter x: ")
y = input("Enter y: ")
x = int(x)
y = int(y)

ans = (1 - math.tan(x))**(1/math.tan(x))+math.cos(x-y)
print(ans)
