from random import randint
mass=[randint(-100, 100) for a in range(20)]
print(mass)
i=0
while (i!=len(mass)):
    if mass[i]%7==0:
        del mass[i]
    else:
        i+=1
print(mass)
i=0
while (i!=len(mass)):
    if mass[i]%2!=0:
        mass.insert(i+1,0)
    i+=1
print(mass)