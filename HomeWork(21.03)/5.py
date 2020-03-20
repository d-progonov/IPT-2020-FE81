a = input("Введите первое число: ")
b = input("Введите второе число: ")
c = input("Введите третье число: ")
a = float(a)
b = float(b)
c = float(c)
if a == b or b == c or c == a:
    a += 5
    b += 5
    c += 5
    print(a, b, c)
else: print("Равных нет")
