from func import Rational

# Создаём два объекта рациональных чисел:
fil = open('data.txt', 'r')
x1 = int(fil.readline())
y1 = int(fil.readline())
r1 = Rational(x1, y1)

x2 = int(fil.readline())
y2 = int(fil.readline())
r2 = Rational(x2, y2)

# Проверяем перегруженную операцию сложения:
r3 = r1 + r2 

# Проверяем перегруженный метод вывода: 
filres = open('results.txt', 'w')
filres.write(str(r3))
filres.write('\n')
print(r3)

# Проверяем перегруженную операцию уножения:
r4 = r1 * r2
filres.write(str(r4))
filres.write('\n')
print(r4)

# Проверяем метод сокращения числа:
r5 = r1.reduce()
filres.write(str(r5))
filres.write('\n')
print(r5)

fil.close()
filres.close()