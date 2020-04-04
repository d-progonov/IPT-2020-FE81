
def sum_geom_progr(N, first, znam):
    return (first*(1-pow(znam,N)))/(1-znam)


try:
    n = abs(int(input("Количество элементов в прогрессии: ")))
    if n != 0:
        first = float(input("Первый элемент прогрессии: "))
        if n == 1:
            print("В Вашей прогрессии 1 элемент, сумма -", first)
        else:
           step = float(input("Знаменатель прогрессии: "))
           print("Сумма",n, "членов Вашей геометрической прогрессии -", round(sum_geom_progr(n, first, step),3))
    else:
        print("В Вашей прогрессии 0 элементов, сумма - 0")

except ValueError:
    print("Ошибка! Проверьте данные и попробуйте снова!")
