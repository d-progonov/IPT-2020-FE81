import math

def task(b,n):
    down_or_up = True
    count = 0
    countp = 0
    pov = False
    row = 0
    colum = 0
    a=[0]*n
    for i in range(n):
        a[i] = [0]*n
    povoroty=n*2-2
    while(row!=n-1)or(colum!=n-1):
        if down_or_up:
            a[row][colum]=b+count
            count=count+b
            if(colum-1<0) or (row+1>n-1):
                down_or_up=False
                row=row-1
                colum=colum+1
                countp=countp+1
                pov=not pov
                pov1=True
            row=row+1
            colum=colum-1
        else:
            a[row][colum] = b+count
            count = count + b
            if(colum+1>n-1)or(row-1<0):
                down_or_up=True
                colum=colum-1
                row=row+1
                countp = countp + 1
                pov = not pov
                pov1 = True
            row=row-1
            colum=colum+1
        if(pov1):
            if(povoroty==((countp-1)*2)):
                pov=not pov
            if pov:
                row=row+1
            else:
                colum=colum+1
            pov1=False
    a[n-1][n-1]=b+count
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()

def b():
    while 1:
        try:
            b=int(input("Enter a number: "))
        except ValueError:
            print("Error; please enter a number")
            continue
        if math.isinf(b):
            print("Error; number can not be an infinite")
            continue
        elif math.isnan(b):
            print("Error; number can not be NanN")
            continue
        else:
            break
    return b

def n():
    while 1:
        try:
            n=int(input("Enter a size of matrix: "))
        except ValueError:
            print("Error, please enter a number")
            continue
        if n<=0:
            print("Number must be posotive")
            continue
        if math.isinf(n):
            print("Error; number cannot be an infinite")
            continue
        elif math.isnan(n):
            print("Error; number cannot be NaN")
            continue
        else:
            break
    return n

if __name__ =="__main__":
    n=n()
    b = b()
    task(b,n)


