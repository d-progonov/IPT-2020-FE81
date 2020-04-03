from random import randint
c = [n for n in range(1,randint(1,10)+1)]
b=[n for n in range(1,pow(len(c),2)+1)]
m=int(pow(len(b),0.5))
a=[[0 for i in range(0,m)] for j in range(0,m) ]
print(c)
k=1
i=m-1
j=0
a[j][i]=b[0]
while(((i!=0) or (j!=m-1))):
    
    if (i==m-1)&(j!=m-1):           #вниз справа
        j+=1
        a[j][i]=b[k]
        k+=1
    while (j!=0 and i!=0):          #вверх по диагонали
        j-=1
        i-=1
        a[j][i]=b[k]
        k+=1
        if (i==0)&(j!=m-1):         #вниз слева
            j+=1
            a[j][i]=b[k]
            k+=1
    if (j==0)&(i!=0):               #сдвиг влево вверху
        i-=1
        a[j][i]=b[k]
        k+=1
    while((i!=m-1)and(j!=m-1)):     #спуск по диагонали
        i+=1
        j+=1
        a[j][i]=b[k]
        k+=1
        if (j==m-1):                #сдвиг влево внизу
            i-=1
            a[j][i]=b[k]
            k+=1
print("Result: ")
for i in range(0, m):
    print(a[i])