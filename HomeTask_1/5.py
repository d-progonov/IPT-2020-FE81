'''
Составить алгоритм увеличения всех трех, введённых с клавиатуры, переменных на 5,
если среди них есть хотя бы две равные. В противном случае выдать ответ «равных нет».
'''

first  = int(input("First  number is: "))
second = int(input("Second number is: ")) 
third  = int(input("Third number  is: "))
 
if (first == second or first == third or third == second):
  first  += 5
  second += 5
  third  += 5
  print("All numbers: ", first, " ", second, " ", third)
else:
  print("Nothing changes")
