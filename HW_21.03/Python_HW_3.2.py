#from numpy import diag, arange
#Z = diag(arange(1, 5), k=-1)
#print(Z)

while(1):
    try:
        n = int (input("Enter n = "))
        if n<1:
            raise ValueError
        break
    except Exception:
        print("Wrong data type for variable a (must be natural int).")

a = [[0] * n for i in range(n)]
moveup = False
movedown = False

col = 0
row = 0
for i in range(1, n*n+1):
    a[row][col] = i
    if col == 0 and row != n-1 and moveup == False:
        row += 1
        moveup = True
        movedown = False
    elif row == 0 and col != n-1 and movedown == False:
        col+=1
        movedown = True
        moveup = False
    elif row == n-1 and moveup == False:
        col+=1
        moveup = True
        movedown = False
    elif col == n-1 and movedown == False:
        row+=1
        movedown = True
        moveup = False
    else:
        if moveup == True:
            col+=1
            row-=1
        if movedown == True:
            col-=1
            row+=1

for i in range(n):
    print(a[i])
input("Any key to exit...")