import numpy as np 

def tran(Arr, m, n):
    if (not(m == n)):
        print(False)
        print("Error. Variables 'm' and 'n' must be equal to provide simetric transpose!")
        return 0

    else:
        k = 1
        for i in range(0, n-1):
            for j in range(k, n):
                Arr[i][j], Arr[j][i] = Arr[j][i], Arr[i][j]
            k = k + 1
        return Arr

def out(Arr):
    print("Your matrix is:")
    for elem in Arr:
        print(elem)
    print("\n") 

try:
    m = int(input("Enter the number of rows: " ))
    n = int(input("Enter the number of col's: " ))

    #Arr = [[ 'a' for i in range(1, m+1)] for j in range(1, n+1)] 
    Arr = [[(str(input("Input elem: "))) for i in range (1, m+1)] for j in range(1, n+1)]
    print("\n")
    out(Arr)

    Arr = tran(Arr, m, n)
    out(Arr)

    string = []
    k = 1; s = '';
    for i in range(0, n-1):
        for j in range(k, n):
            s = s + Arr[i][j]
        string.append(s)
        s = ''; k = k + 1;
    print("String is", string)

except ValueError:
    print("Wrong input data.")
