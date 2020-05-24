import math


def fast_exp(a, n):

    def even(n):

        if n % 2 == 0:

            return 1

        return 0

    if n == 0:

        return 1

    if even(n):

        return fast_exp(a, n / 2) ** 2

    return a * fast_exp(a, n - 1)



while True:

    try:

        B = input("Введите любое рациональное число:")

        if B == "pi":

            a = math.pi

            break

        elif B == "e":

            a = math.e

            break

        elif B == "inf":

            a = float('inf')

        elif B == "nan":

            if_nan()

            continue

        a = float(B)

        break

    except valueError:

        print("Введено неверное значение")



while True:

    try:

        n = float(input("ВВедите степень:"))

        if not n > 0 or n % 1 != 0:

            print("Степень должна быть положительной")

            continue

        break

    except ValueError:

        print("Введено неверное значение")



if __name__ == '__main__':

    print(fast_exp(a, n))
