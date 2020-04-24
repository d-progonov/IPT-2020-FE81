import numpy as np

def trimax(s, n, Nstr):

    if (not(len(s) == Nstr)):
        print(False)

    a = []; b = []; c = []
    i = 0
    for elem in s:
        if i < n: 
            a.append(elem)
        if n <= i < (n + (n-1)): 
            b.append(elem)
        if (n + (n-1)) <= i < Nstr: 
            c.append(elem)
        i = i + 1

    l_a = 0; l_b = 0; l_c = 0

    M = np.chararray((N, N), unicode=True)
    M[:] = '0'
    print(M)
    
    print("------------------------------------------------------")
    print()

    for i in range(0, N):
        for j in range(0, N):
            if (i == j):
                M[i][j] = a[l_a]
                l_a += 1
            if ((j-i) == 1):
                M[i][j] = b[l_b]
                l_b += 1
            if ((i-j) == 1):
                M[i][j] = c[l_c]
                l_c += 1
    return M

def transpose(n, m):
    if (n % 2 == 0):
        print("Error! Can't determine the middle row.")
        print("Order of matrix must be odd number.")
        return 0
    else:
        middle = int((n / 2) - 0.5)
        print("Middle is: ", middle)
                
        for row in range(0, middle):            
            m[:,[row, N-row-1]] = m[:,[N-row-1, row]]
        return m

def сoncatenation(m, a, b):
  string1 = m[a]
  string2 = m[b]
  string = (''.join(string1)) + (''.join(string2)) 
  return string

N = int(input(" Enter order of matrix: "))
Nstr = N + (N-1) + (N-1)
print("\n", "Enter String Const. Length must be:", Nstr)
string = str(input(" String: "))

TriMartix = trimax(string, N, Nstr)
print("TriMartix: ")
print(TriMartix)
print()

TransMatrix = transpose(N, TriMartix)
print("TransMatrix: ")
print(TransMatrix, '\n')

print("Enter two rows, which you want to concatenate.")
A = int(input(" Enter the first one: "))
B = int(input(" Enter the second one: "))
ConcatMatrix = сoncatenation(TransMatrix, A, B)
print("ConcatString: ", ConcatMatrix)