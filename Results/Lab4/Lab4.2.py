mas = []
start = True
def push(temp):
    mas.append(temp)
    print("Наш стек має вигляд:")
    for i in range(1,len(mas)+1):
        print(mas[-i])
def pop():
    ans = mas.pop()
    print("Наш стек має вигляд:")
    for i in range(1,len(mas)+1):
        print(mas[-i])
    return ans
while start:
    print("Щоб працювати зі стеком, оберіть потрібний метод:\nНатисніть 1 щоб добавити елемент у стек;\nНатисніть 2 щоб отримати елемент зі стека.")
    i = True
    while(i):
        ans = input("(1 або 2):\t")
        if ans == "1":
            j = True
            while(j):
                print("Введіть елемент, який хочете помістити у стек:")
                elem = input()
                while elem == "":
                    print("Введіть елемент ще раз:")
                    elem = input()
                j = False
            push(elem)
            i = False
        elif ans == "2":
            if len(mas) == 0:
                print("Стек порожній")
            else:
                ans = pop()
                print("Ми отримали елемент:", ans)
            i = False
        else:
            print("Оберіть метод 1 або 2")
    print("Хочете продовжити роботу?")
    k = True
    while(k):
        a = input("(y/n):\t")
        if a == "y":            
            k = False
        elif a == "n":
            start = False
            k = False
        else:
            print("Напишіть так (y) чи ні (n)")
    
