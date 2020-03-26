
import math
import numpy as np

while True:
    try:
        size = int(input("Input array size:"))
        break
    except ValueError:
        print("Invalid value entered!")

matrix = np.array([[0 for _ in range(size)] for _ in range(size)])

for i in range(size):
    for j in range(size):
        while True:
            try:
                matrix[i][j] = int(input("Input matrix[{}][{}]".format(i, j)))
                break
            except ValueError:
                print("Invalid value entered! Natural numbers only! Please, input another value:")

taken = matrix

start = 0
end = size

for i in range(size):
    for k in range(start, end):
        taken[i][k] = (matrix[i][k]) ** 2
    start += 1
    end -= 1

final = np.array(taken)

started = 0
finished = size

for m in range(size - 1, -1, -1):
    for z in range(finished - 1, started - 1, -1):
        final[m][z] = (taken[m][z]) ** 2
    started += 1
    finished -= 1

print(final)

