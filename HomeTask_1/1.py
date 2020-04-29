''' 
Составить программу, которая будет считывать введённое пятизначное число. 
После чего, каждую цифру этого числа необходимо вывести в новой строке.
'''

N = 1000

try:
  n = int(input("Number is: "))

  if (n < 1000):
    print("\n", "Error: invalid input value.")
    print("The n must be five-digit number!")

  else: 
    while(N > 1 or N == 1):
      print(int (((n//N) % 10)))
      N = N/10

except ValueError:
  print("\n", "Error: invalid syntax.")
  print(" Data must be numeric!")