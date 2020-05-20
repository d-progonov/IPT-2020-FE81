n = int(0)
x = float(0)
y = float(0)
while (True):
    if(n > 1):
        x = (n)/((n-1)**2)
        y = x
    else:
        x = 1
        y += 0
    n += 1
    if (abs(x)<0.0001):
        break
print("Sum_({0}) = {1}".format(n, y))
