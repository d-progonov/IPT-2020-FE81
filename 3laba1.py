import math


some_magic = 0.3


def get_next_element(n):
    return math.factorial(n) / (3 * (n ** n))


if __name__ == "__main__":

    # pre-init local variables
    accuracy = 1e-4
    sum = 0
    n = 1

    # input data
    while True:
        a = input(" Точность: ")
        try:
            accuracy = float(a)
        except (TypeError, ValueError):
            print('Это не число')
            continue

        if math.isnan(accuracy):
            print("Невозможно выполнить действия с не числом (NaN). Введите число.")
        elif accuracy <= 0:
            print("Точность должна быть положительным числом")
        elif accuracy == math.inf:
            print("Точность не может быть бесконечностью")
        elif accuracy > some_magic:
            print("Нельзя обработать ")
        else:
            print('Число а = ', accuracy)
            break

    s = get_next_element(n)
    sum += s
    while abs(get_next_element(n) - get_next_element(n+1)) >= accuracy:
        n += 1
        s = math.factorial(n) / (3 * n ** n)
        sum += s
        print(s)

    print("Cумма: {:.10f}".format(sum))