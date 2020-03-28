#очень вовремя сходил в душ

def fibon(n):
    if n < 0:
        print("wrong input")
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    return fibon(n - 1) + fibon(n - 2)


for i in range(0, 1001, 1):
    print("# ", i, fibon(i))

for i in range(0, 10001, 1):
    print("# ", i, fibon(i))