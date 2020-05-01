maxLen = []

def get_answ():
    return maxLen

def is_digit(temp):
    if temp.isdigit():
       return True
    else:        
        try:
            int(temp)
            return True
        except ValueError:
            print(temp,"не ціле число")
            return False

def is_degree(elem):
    if elem > 0:
        elem = str(elem)
        if elem[-1] == "5":
            while elem[-1] == "5":
                elem = int(elem) / 5                
                elem = str(elem)
                elem = elem[:-2]
            elem = int(elem)
            if elem == 1:
                return True
            else: return False
        elif len(elem) == 1 and elem == "1":
            return True
        else: return False   

def fun(mas, x, answ):    
    while is_degree(mas[x]) and x < len(mas)-1:        
        answ += 1
        x += 1
    maxLen.append(answ)
    answ = 0
    return x

if __name__ == "__main__":
    n = input("Введіть довжину послідовності n:\t")
    answ = 0
    num = []    

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
                print("Довжина максимальної послідовності із ступенів числа 5:",max(maxLen))
                
    
    
