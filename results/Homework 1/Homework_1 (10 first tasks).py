#Деление числа на разряды
x = int(input('x = '))

y = 0
while x > 0:
	digit = x % 10;
	x = x // 10
	y = y * 10 
	y = y + digit

while y > 0:
    n = y % 10
    y = y // 10
    print(n)


#Запрограммировать математическое выражение
a, b, f = int(input('\na = ')), int(input('b =')), int(input('f ='))
c = (a + b - f / a) + f * a * a - (a + b)
print ('c = (а + b — f / а) + f * a * a — (a + b) = ', c)


#Прямоугольный треугольник
print ('\n+\n++\n+++\n++++\n+++++\n++++++\n+++++++\n++++++++\n+++++++++\n')


#Сравнение чисел используя оператор ветвления
fir, sec = int(input('first = ')), int(input('second ='))

if fir > sec:
    print ('больше\n')

elif fir < sec:
    print ('меньше\n')

else:
    print ('Эти числа равны\n')


#Увеличение переменных с оператором if
one, two, free = int(input('one = ')), int(input('two =')), int(input('free ='))
if one == two or one == free or two == free or one == two == free:
    one += 5
    two += 5
    free += 5
    print (one, two, free)
else:
    print ('Равных нет')


#Алгебраическая сумма
N, k = int(input('\nN = ')), int(input('k ='))

sum = 0
for i in range(1, N+1):
    sum = i**k + sum

print(sum, '\n')


#Большая и меньшая цифры числа
num = int(input('num = '))
n = num % 10
num = num // 10
print(n, 'is bigger\n') if n > num else print(num, 'is bigger\n')


#Возведение числа в степень
z, v = int(input('z = ')), int(input('v ='))
def power(z, v):
    if v < 0:
        z = 1 / z
        v = -v

    res = 1
    while v > 0:
        res = res * z
        v = v - 1
    return res

print (power(z,v))


#Вычислить длину вектора
import math
x1, y1, z1 = int(input('\nx = ')), int(input('y =')), int(input('z ='))

length = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)

print('Length = ', length)


#Значение выражения (1-tg x)^(ctg x)+ cos(x-y)
import math
x2, y2 = float(input('\nx = ')), float(input('y ='))
print((1 - math.tan(x2)) ** (math.cos(x2)/math.sin(x2)) + math.cos(x2 - y2))