def compression(a):
    out = ""
    c = 1
    if len(a)==1:
        return a
    for i in range(len(a)):
        if i==(len(a)-1):
            if c!=1:
                out+=a[i]+"("+str(c)+")"
            else:
                out+=a[i]
        else:
            if a[i]==a[i+1]:
                c+=1
            else:
                if c!=1:
                    out+=a[i]+"("+str(c)+")"
                    c=1
                else:
                    out+=a[i]
    return (out)

while(1):
    try:
        a = str (input("Enter string: "))
        break
    except Exception:
        print("Unable to read string.")
print("Compressed string:", compression(a))
input("Any key to exit...")
