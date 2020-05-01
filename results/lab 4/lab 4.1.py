import numpy as np
n = int(input("Enter n = "))
if n % 4 != 0:
    n = input("This 'n' value can`t create 2n! matrix")
arr = np.arange((n ** 2)).reshape(n, n)
print("Array before transformation:    ", arr, sep='\n')
middle = int(n / 2)
left_1 = arr[:middle, :middle]
right_1 = arr[:middle, middle:n]
left_2 = arr[middle:n, :middle]
right_2 = arr[middle:n, middle:n]

aft_arr = np.array(arr)
aft_arr[:middle, :middle] = right_2
aft_arr[:middle, middle:n] = left_2
aft_arr[middle:n, middle:n] = left_1
aft_arr[middle:n, :middle] = right_1

print("Array after transformation: ", aft_arr, sep='\n')
