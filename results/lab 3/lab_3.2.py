def factorial(i):
    if i == 0:
        return 1
    return factorial(i-1) * i

try:
    n = int(input("Введите количество ваших элементов: "))

    A = []

    product = 0    
    for i in range(0, n):
        elem = int(input("Введите элемент: "))
        A.append(elem)
    
    k = 1
    product = 1    
    for elem in A:
        print(elem, ' ', end = '')
        if k + 1 < elem < factorial(k):
            product = product * elem
            k += 1
        else:
            k += 1
    print("\nРезультат программы: ", product)

except ValueError:
    print("Ошибка ввода! Проверьте вводимые данные и попробуйте еще раз!")
