while(1):
    try:
        a = str (input("Enter original string: "))
        break
    except Exception:
        print("Unable to read string.")
while(1):
    try:
        b = str (input("Enter string to find: "))
        break
    except Exception:
        print("Unable to read string.")
i = 0
found = 0
j = 0
while(i<len(a)):
    if j == len(b):
        found+=1
        j=0
    elif a[i] == b[j]:
        j+=1
    else:
        j=0
    i+=1
if j == len(b):
    found+=1
print("Number of times string\n'"'{}'"'\nwas found in\n'"'{}'"'\nis:\n".format(b,a), found, sep='')
input("Any key to exit...")