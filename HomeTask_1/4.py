'''
Составить программу, которая требует ввести два числа. 
Если первое число больше второго, то программа печатает слово больше. 
Если первое число меньше второго, то программа печатает слово меньше. 
А если числа равны, программа напечатает сообщение Эти числа равны.
'''

first  = int(input("First  number is: "))
second = int(input("Second number is: ")) 
 
if first > second:
    print("Bigger")
 
elif first < second:
    print("Smaller")
 
elif first == second:
    print("Numbers are equal")
