sum = 0
n = 1
i = True
while(i):
    s = (2*n-1)/2**n
    if s < 1*10**-4:
        i = False
    else:
        sum += s
        n += 1
sum = round(sum, 4)
print("Summ: ", sum)
