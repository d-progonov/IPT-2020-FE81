def work():
    string = str(input("Уведите входную строку"))
    result = list(string)
    print(result)
    elem = str(input("Уведите искаемый елемент"))
    n = len(result)
    curr = 0
    for i in range(n):
        if result[i] == elem:
            curr += 1
    print("Количество повтяйщихся элементов: ", curr)



if __name__ == "__main__":
    work()
