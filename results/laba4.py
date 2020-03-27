
n=4
a=[['a','a','b','a'],['a','a','c','c'],['b','c','a','a'],['b','b','c','b']]

Acounter=0
Bcounter=0

try:
    n=int(n)

    for row in a:
        print(' '.join([str(elem) for elem in row]))
    print()
    for i in range(n):
        for j in range(n):
            if i<j:
                if a[i][j]=='a':
                    Acounter+=1
                    a[i][j] = '*'
            if i + j > n - 1:
                    if a[i][j]=='b':
                        Bcounter+=1
                        a[i][j]='*'



except ValueError:print("Введите другое значаение для n!!!")
for row in a:
    print(' '.join([str(elem) for elem in row]))
print(Acounter)
print(Bcounter)