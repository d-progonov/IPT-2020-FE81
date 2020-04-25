def check(NUM):
    check_help = True
    try:
        num_1 = int(NUM)
    except ValueError:
        print("Error, уведите целое или дробное число")
        check_help = False
    return check_help


while 1:
    a = input("Уведите значение а: ")
    if check(a) == False:
        continue
    b = input("Уведите значение b: ")
    if check(b) == False:
        continue
    c = input("Уведите значение c: ")
    if check(c) == False:
        continue
    d = input("Уведите значение d: ")
    if check(d) == False:
        continue
    else:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(c)
        for x in range(1, d // a):
            for y in range(1, d // b):
                for z in range(1, d // c):
                    if x * a + y * b + z * c == d:
                        print('Иначе ответ:  x = {0}, y = {1}, z = {2}'.format(x, y, z))
