# Part A
def nsd(m, n):
    if n == 0:
        return m
    else:
        return nsd(n, m % n)

# Part B
def A(n, m):
    if n == 0:
        return m + 1
    if n != 0 and m == 0:
        return A(n - 1, 1)
    if n > 0 and m > 0:
        return A(n - 1, A(n, m - 1))
