import random
D = input("Enter D: ")
a=[]

try:
    size = random.randint(3, 20)
    print("Size:", size)
    print()
    D=int(D)
    i=0
    for i in range(size):
        a.append(random.randint(1,100))
    print("a:", a)
    del a[0]
    print("a:", a)

    if D>0:
        for i in range(D):
            a.insert(0,a.pop())
            print("a:", a)
    else:print("Введите другое значаение для D!!!")



except ValueError:print("Введите другое значаение для D!!!")
