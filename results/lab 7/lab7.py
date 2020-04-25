n = int(input("Enter n:"))
cup=[]
lis = []
for i in range(0,20):
    cup.append(0)
for i in range (0,n) :
    s = input("Enter word:")
    if s.__len__() > 20:
        s = input("Enter word again length should be less than 20!:")
    lis.insert(i, s)
for i in range (len(lis)):
    for j in range(0,20):
        if len(lis[i]) == j:
            cup[j] += 1
for i in range(len(cup)):
    if cup[i] != 0:
        print(i, " symbol = ", cup[i])
print("Word count is :", len(lis))






