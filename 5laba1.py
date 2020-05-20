if __name__ == "__main__":

    while True:
        inputString = input("Введите строку: ")
        if len(inputString) == 0:
            print("Строка пустая...")
            continue
        if '1' not in inputString and '0' not in inputString:
            print("В строке отсутсвуют 0 и 1")
            continue
        else:
            break

    while True:
        inPos = input("Введите позицию, с которой нужно начать: ")
        try:
            i_inPos = int(inPos)
        except ValueError:
            print("Вы ввели не цифру.")
            continue
        if i_inPos <= 0:
            print("Позиция не может быть отрицательной или 0.")
            continue
        if i_inPos > len(inputString):
            print("Длина строки меньше, чем введённая позиция.")
            continue
        else:
            break
    lst = list(inputString)
    for i in range(i_inPos - 1, len(lst)):
        if lst[i] == '0':
            lst[i] = '1'
        elif lst[i] == '1':
            lst[i] = '0'
    print("Результат: " + ''.join(lst))
