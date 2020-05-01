n = int(input("Введите верхнюю границу интервала: "))
sum=0

for i in range(1,n):
    curr=i**3-3*i*(n**2)+n   # curr=15
    res=curr/3               # res=5
    print(i, "-элемент -", curr)
    if(curr%3==0):             
        if(not(res%2)==0):        # нечетность
            sum=curr+sum
print(float(sum))