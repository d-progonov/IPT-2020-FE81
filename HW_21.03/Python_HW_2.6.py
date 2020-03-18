while(1):
    try:
        hH = float (input("Enter hole height = "))
        if hH<0:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for hole height (must be positive float).")
while(1):
    try:
        hW = float (input("Enter hole width = "))
        if hW<0:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for hole width (must be positive float).")

while(1):
    try:
        bH = float (input("Enter brick height = "))
        if bH<0:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for brick height (must be positive float).")
while(1):
    try:
        bW = float (input("Enter brick width = "))
        if bW<0:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for brick width (must be positive float).")
while(1):
    try:
        bD = float (input("Enter brick depth = "))
        if bD<0:
            raise ValueError
        break
    except ValueError:
        print("Wrong data type for brick depth (must be positive float).")

hSize = [hH, hW]
bSize = [bH, bW, bD]

for elem in bSize:
    if elem == max(bSize):
        del bSize[bSize.index(elem)]
        break

a = max(hSize)
b = min(hSize)
p = max(bSize)
q = min(bSize)

if b>q and a>p:
    print("Войдет непосредственно.")
elif max(bSize)>max(hSize) and b>=(2*p*q*a+(p*p-q*q)*pow((p*p+q*q-a*a),0.5))/(p*p+q*q):
    print("Войдет с наклоном.")
else:
    print("Никак не войдет.")
input("Any key to exit...")