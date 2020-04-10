import numpy as np

b = list(map(int, input('Enter characters separated by comma: ').split(',')))
n = len(b)

a = np.zeros((n, n), dtype=int)
i = 0
r = 0
c = n - 1

def check(y):
    y += 1
    if y == n:
        y = 0
    return y

if n == 1:
    a[0][0] = b[0]

elif n % 2 == 0:

    while r != n and c != 0:
        if r == 0 and c == n - 1:
            a[r][c] = b[i]
            i = check(i)
            r += 1

        if 0 < r < n - 1 and c == n - 1 and r % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            r -= 1
            c -= 1

        if 0 < r < n - 1 and c == n - 1 and r % 2 == 0:
            a[r][c] = b[i]
            i = check(i)
            r += 1

        if r == 0 and 0 < c < n - 1 and c % 2 == 0:
            a[r][c] = b[i]
            i = check(i)
            c -= 1

        if r == 0 and 0 < c < n - 1 and c % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            c += 1
            r += 1

        if 0 < r < n - 1 and 0 < c < n - 1 and c % 2 == 1 and r % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            c -= 1
            r -= 1

        if 0 < r < n - 1 and 0 < c < n - 1 and r % 2 == 0 and c % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            r += 1
            c += 1

        if 0 < r < n - 1 and 0 < c < n - 1 and r % 2 == 1 and c % 2 == 0:
            a[r][c] = b[i]
            i = check(i)
            r += 1
            c += 1

        if 0 < r < n - 1 and 0 < c < n - 1 and c % 2 == 0 and r % 2 == 0:
            a[r][c] = b[i]
            i = check(i)
            c -= 1
            r -= 1

        if r == 0 and c == 0:
            a[r][c] = b[i]
            i = check(i)
            r += 1


        if r == n - 1 and c == n - 1:
            a[r][c] = b[i]
            i = check(i)
            c -= 1
            r -= 1

        if r == n - 1 and 0 < c < n - 1 and c % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            r -= 1
            c -= 1

        if r == n - 1 and 0 < c < n - 1 and c % 2 == 0:
            a[r][c] = b[i]
            i = check(i)
            c -= 1

        if 0 < r < n - 1 and c == 0 and r % 2 == 0:
            a[r][c] = b[i]
            i = check(i)
            r += 1

        if 0 < r < n - 1 and c == 0 and r % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            r += 1
            c += 1

        if r == n - 1 and c == 0:
            a[r][c] = b[i]
            r += 1
else:
    while r != n and c != 0:
        if r == 0 and c == n - 1:
            a[r][c] = b[i]
            i = check(i)
            r += 1

        if 0 < r < n - 1 and c == n - 1 and r % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            r -= 1
            c -= 1

        if r == 0 and 0 < c < n-1 and c % 2 == 0:
            a[r][c] = b[i]
            i = check(i)
            c += 1
            r += 1

        if 0 < r < n - 1 and 0 < c < n - 1 and c % 2 == 1 and r % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            c += 1
            r += 1

        if r % 2 == 0 < r < n - 1 == c:
            a[r][c] = b[i]
            i = check(i)
            r += 1

        if 0 < r < n - 1 and 0 < c < n - 1 and r % 2 == 0 and c % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            r -= 1
            c -= 1

        if 0 < r < n - 1 and 0 < c < n - 1 and r % 2 == 1 and c % 2 == 0:
            a[r][c] = b[i]
            i = check(i)
            r -= 1
            c -= 1

        if r == 0 and 0 < c < n - 1 and c % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            c -= 1

        if r == 0 and c == 0:
            a[r][c] = b[i]
            i = check(i)
            r += 1
            c += 1

        if 0 < r < n - 1 and 0 < c < n - 1 and c % 2 == 0 and r % 2 == 0:
            a[r][c] = b[i]
            i = check(i)
            c += 1
            r += 1

        if r == n - 1 and c == n - 1:
            a[r][c] = b[i]
            i = check(i)
            c -= 1

        if r == n - 1 and 0 < c < n - 1 and c % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            r -= 1
            c -= 1

        if r == n - 1 and 0 < c < n - 1 and c % 2 == 0:
            a[r][c] = b[i]
            i = check(i)
            c -= 1

        if r > 0 < n - 1 and c == 0 and r % 2 == 1:
            a[r][c] = b[i]
            i = check(i)
            r += 1

        if 0 < r < n - 1 and c == 0 and r % 2 == 0:
            a[r][c] = b[i]
            i = check(i)
            c += 1
            r += 1

        if r == n - 1 and c == 0:
            a[r][c] = b[i]
            r += 1

for r in a:
    print(r)
