import random
n = input("Enter n: ")
a=[]

try:
    size = random.randint(3, 20)
    print("Size:", size)
    print()
    n=int(n)
    i=0
    for i in range(size):
        a.append(random.randint(1,100))
    print("a:", a)
    del a[0]
    print("a:", a)

    if n<0:
        n=abs(n)
        for i in range(n):
            a.append(a.pop(0))
    else:
        for i in range(n):
            a.insert(0,a.pop())
    print("a:", a)

except ValueError:print("Введите другое значаение для n!!!")
