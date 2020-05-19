import numpy as np

def invert(n, m):
    if (n % 2 == 0):
        print("Error! Can't determine the middle row.")
        return 0
    else:
        mid = int((n / 2) - 0.5)
        for row in range(0, mid):            
            m[[row, n-row-1],:] = m[[n-row-1, row],:]
        return m

n = int(input("n: "))
m = int(input("m: "))

M = np.chararray((n, m), unicode=True)

# Char-element Fill 
# e = str(input("Enter char to fill matrix: "))
# M[:] = e

# Keyboard elements fill:
for i in range(n):
  for j in range(m):
    M[i][j] = str(input("e: "))
    
print(M, "\n")

invM = invert(n, M)
print("Invert Matrix is:")
print(invM, "\n")

string = []
for i in range(n):
  for j in range(m):
    string.append(invM[i][j])

print("String var is: ", string, "\n")

L = len(string)
print("Lenght of String is: ", L, "\n")