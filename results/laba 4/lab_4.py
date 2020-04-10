import numpy as np

def work():
    while (1):
        try:
            n = int(input("Enter n = "))
            if n % 4 != 0:
                raise ValueError
            break
        except ValueError:
            print("Даное число не создаст матрицу размерности 2n!")
        except Exception:
            print("Ошибка, уведите целое число ")

    arr = np.arange((n ** 2)).reshape(n, n)
    print("List:    ", arr, sep='\n')

    middle = int(n / 2)
    left_1 = arr[:middle, :middle]
    right_1 = arr[:middle, middle:n]
    left_2 = arr[middle:n, :middle]
    right_2 = arr[middle:n, middle:n]

    ex_arr = np.array(arr)
    ex_arr[:middle, :middle] = left_2
    ex_arr[:middle, middle:n] = right_2
    ex_arr[middle:n, middle:n] = right_1
    ex_arr[middle:n, :middle] = left_1

    print("Исходный масив: ", ex_arr, sep='\n')

if __name__ == "__main__":
    work()