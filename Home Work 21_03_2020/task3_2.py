def check_h(NUM):
    check_help = True
    try:
        num_1 = float(NUM)
    except ValueError:
        print("Ошибка, уведите целое или дробное число")
        check_help = False
    return check_help


def isZeros(matrix):
    for char in matrix:
        if 0 in char:
            return True
    return False


def check():
    global downside, upside, leftside, rightside, downdiag, updiag
    if i == 0:
        downside = False
        upside = True
    if i == n - 1:
        downside = True
        upside = False
    if i != n - 1 and i != 0:
        downside = False
        upside = False
    if j == 0:
        leftside = True
        rightside = False
    if j == n - 1:
        rightside = True
        leftside = False
    if j != n - 1 and j != 0:
        leftside = False
        rightside = False


while 1:
    n = input("n = ")
    if check_h(n) == False:
        continue
    if int(n) <= 1:
        continue
    else:
        n = int(n)
        matrix = [[0] * n for _ in range(n)]

        i = 0
        j = 0

        upside = True
        downside = False
        leftside = True
        rightside = False
        updiag = False
        downdiag = True

        num = 1

        while isZeros(matrix):
            if matrix[i][j] == 0:
                matrix[i][j] = num
                num += 1
            if (i < n - 1 and leftside and downdiag) or (i < n - 1 and rightside and updiag):
                i += 1
                if leftside:
                    downdiag = False
                    updiag = True
                if rightside:
                    DOWNDIAG = True
                    updiag = False
                check()
                continue
            elif (j < n - 1 and upside and updiag) or (j < n - 1 and downside and downdiag):
                j += 1
                if upside:
                    downdiag = True
                    updiag = False
                if downside:
                    downdiag = False
                    updiag = True
                check()
                continue
            elif i > 0 and j < n - 1 and updiag:
                i -= 1
                j += 1
                check()
                continue
            elif i < n - 1 and j > 0 and downdiag:
                i += 1
                j -= 1
                check()
                continue

        for char in matrix:
            print(*char)
        break