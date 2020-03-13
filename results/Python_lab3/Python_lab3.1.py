
n = int(0)
x = float(0)
y = float(0)
while (True):
    x = (2*n-1)/(2**n)
    print("A{:<3} = ".format(n), x)
    y += x
    n += 1
    if (abs(x)<0.001):
        break
print("An=(2n-1)/(2^n)\nAccuracy: 10^-4\nS = {:0.4f}".format(y))
print("({})".format(y))
input("Any key to exit...")