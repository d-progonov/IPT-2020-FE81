import tkinter as tk
import math
import turtle


def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Error, уведите целое или дробное число")
        check_help = False
    return check_help


def is_prime(n):
    check_h = False
    n = int(n)
    i = 2
    j = 0  # флаг
    while (i ** 2) <= n and j != 1:
        if n % i == 0:
            j = 1
        i += 1
    if j == 1:
        print("Это составное число")
        check_h = False
    else:
        print("Это простое число")
        check_h = True
    return check_h


def x(a, b, t):
    x_1 = (a + b) * math.cos(t) - a * math.cos(((a + b) * t) / a)
    return x_1


def y(a, b, t):
    y_1 = (a + b) * math.sin(t) - a * math.sin(((a + b) * t) / a)
    return y_1


def work():
    while 1:
        a = input("Уведите значение а: ")
        if check(a) == False:
            continue
        b = input("Уведите значение b: ")
        if check(b) == False:
            continue
        if is_prime(a) == False:
            continue
        if is_prime(b) == False:
            continue
        if (float(a) / float(b)) <= 0 or (float(a) / float(b)).is_integer() == False:
            print("Дробь из чисел а и б не целая или отрецательная")
            continue

        else:
            a = float(a)
            b = float(b)
            t = 0
            turtle.hideturtle()
            turtle.speed(0)
            turtle.color('green')
            turtle.width(1)

            for i in range(4):  # оси
                turtle.forward(300)
                turtle.backward(300)
                turtle.right(90)

            turtle.color('red')
            turtle.width(2)
            turtle.pu()

            turtle.goto((a + b) * math.cos(t) - a * math.cos(((a + b) * t) / a),
                        (a + b) * math.sin(t) - a * math.sin(((a + b) * t) / a))  # сдвинуть в точку
            turtle.pd()  # pen down

            while 0 <= t < 2 * a * math.pi:
                x1 = x(a, b, t)
                y1 = y(a, b, t)
                turtle.goto(x1, y1)
                t += 0.05
            tk.mainloop()
            input("Уведите любой символ для выхода...")
            break


if __name__ == "__main__":
    work()
