'''
Запрограммировать следующее выражение: (а + b — f / а) + f * a * a — (a + b) 
Числа а , b , f вводятся с клавиатуры. Организовать пользовательский интерфейс, таким
образом, чтобы было понятно, в каком порядке должны вводиться числа.
'''
import time 

try:
  a = float(input("Input a-value: "))
  b = float(input("Input b-value: "))
  f = float(input("Input f-value: ")) 
  print("Calculating...")
  time.sleep(2)
  res = (a + b - f / a) + f*a*a - (a + b)
  print("Result is: ", res)
  print("Thank you!") 

except ValueError:
  print("\n", "Error: invalid syntax.")
  print(" Data must be numeric!")

except ZeroDivisionError:
  print("\n", "Error: invalid input value.")
  print(" Float division by zero!")