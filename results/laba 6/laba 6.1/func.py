def check(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Error, уведите целое или дробное число")
        check_help = False
    return check_help


def square(x1, x2, y1, y2):
    res_1 = abs(float((x1 * y2 - x2 * y1) / 2))
    return res_1