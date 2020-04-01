import numpy as np
import random

def func():
    try:
        n = int(input("Введите размерность матрицы: "))
        v = int(input("Как вы хотите её заполнить? 1 - вручную, 2 - случайным образом."))

        if (v == 1):
            print("Начинайте ввод элементов.")
            m = [[int(input("Elem: ")) for i in range(n)] for i in range(n)]
        elif (v == 2):
            print("Генерация псевдослучайных чисел начата.")
            m = [[random.randint(1, 10) for i in range(n)] for i in range(n)]
        else:
            print("Ошибка. Указан неизвестный вариант.")
            return

    
        print("Вывод матрицы")
        for el in m: 
            print(el)

        B = []

        for i in range(0, n):
            string = ''
            for j in range(0, n):
                elem = str(m[i][j])
                string += elem
            reversed_string = string[::-1]

            if (string == reversed_string):
                B.append(1)
            else:
                B.append(0)

        print("Вывод результата: ")
        print(B)

    except ValueError:
        print("Ошибка. Значения введены неверно.")
func()
   
    



