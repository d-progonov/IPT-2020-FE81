def a(n):
    return n / pow((n - 1), 2)


def lab3():
    print("HI! Lab3!")
    E = pow(10, -4)
    a_sum = 0.0
    n = 2
    while True:
        curr = a(n)
        if curr <= E:
            break
        a_sum += curr
        n += 1

    return a_sum


print(lab3())
