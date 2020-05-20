import math
"""
Якщо розглянути t(x), то можна побачити, що вираз скорочується і по факту ми отримаємо суму типу
1/(2k+1), тому  t(x) результат не залежить від вхідних даних. Відповідно і результат самого виразу
не залежить від вхідних даних.Завдяки цьому зауваженні ще на стадії створення алгоритму можна зменшити
навантаження на комп'ютер. Але в завданні треба було написати функцію, тому я слідував заданому 
завданню.
"""
def exit_func():
   e = input("If you want to end this program, please input \"e\": ")
   if(e.lower() == 'e'):
      raise SystemExit(0)

def t(x):
    sum1 = 0
    sum2 = 0

    for k in range(11):
        sum1 += (x**(2*k + 1))/math.factorial(2*k + 1)
    
    for k in range(11):
        sum2 += (x**(2*k + 1))/math.factorial(2*k + 1)

    return sum1/sum2 

def decision():
    try:
        y = float(input("Enter y pls: "))

        res = (1.7 * t(0.25) + 2 * t(1 + y))/6 - t(y**2 - 1)
        return float(res)

    except ZeroDivisionError:
        print("Zero division, please enter a right y:")
        exit_func()
        decision()
    
    except ValueError:
        print("Plese enter a numberic data")
        exit_func()
        decision()

if __name__ == "__main__":
    print("%.4f" %decision())