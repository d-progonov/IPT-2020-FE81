from Lab5_1 import is_digit, is_degree, fun, get_answ

n = input("Введіть довжину послідовності n:\t")
answ = 0
num = []
t = []

if is_digit(n):
    n = int(n)
    if n > 0:
        for i in range(n):
            temp = input("Введіть елемент послідовності:\t")
            if is_digit(temp) == True:
                temp = int(temp)
                num.append(temp)
        y = 0
        if n == 1:
            if is_degree(num[0]):
                print("Довжина максимальної послідовності із ступенів числа 5: 1")
            else: print("Довжина максимальної послідовності із ступенів числа 5: 0")
        else:
            while y < len(num)-1:
                y = fun(num,y,answ)
                y +=1
            if y == len(num):
                if is_degree(num[y-1]):
                    t = num.pop()
                    t += 1
                    num.append(t)
            t = get_answ()            
            print("Довжина максимальної послідовності із ступенів числа 5:",max(t))
        
