for i in range(1,100):
    k=str(i)
    for j in range(0,round(len(k)/2)+1):
        if k[j]!=k[-j-1]:
            break
        if j==round(len(k)/2):
            print(i)