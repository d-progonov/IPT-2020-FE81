stringlist = []
a = 1
while a != '0':
    a = str(input("Enter string(0 to stop):"))
    stringlist.append(a)
del stringlist[len(stringlist)-1]
print(stringlist)

found = []
i = 1
for s in stringlist:
    if s.find(stringlist[0]) != -1:
        if i == 1:
            i+=1
            continue
        found.append(i)
    i+=1

print(found)


for i in found:
    while stringlist[i-1].find(stringlist[0]) != -1:
        j = stringlist[i-1].find(stringlist[0])
        stringlist[i-1]=stringlist[i-1][:j]+stringlist[i-1][j+len(stringlist[0]):]



for j in range(len(stringlist)):
    i=0
    while(i!=len(stringlist[j])):
        if stringlist[j][i] == ' ':
            stringlist[j] = stringlist[j][:i] + stringlist[j][i+1:]
        else:
            i+=1

print(stringlist)