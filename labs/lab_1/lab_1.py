import math

def exit_func():
   e = input("If you want to end this program, please input \"e\": ")
   if(e.lower() == 'e'):
      raise SystemExit(0)

def decision():
   try:
      x = float(input("Please, input x: "))
      z = float(input("Please, input z: "))
      y = ((2*x**2 + x -5)/x+2) +1/math.tan(x/2*z)

      print("The answer is: %.2f" % y)

   except ValueError:
      print("\nYou have to enter only a number. Please, repeat your input.")
      exit_func()
      decision()

   except ZeroDivisionError:
      print("\nYou entered a denomintor(z) zero. Please, repeat your input.")
      exit_func()
      decision()
   

if __name__ == "__main__":
    decision() 