#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from inc.errorhandling import handle
import math

def my_pow(a, n):
  return 1 if n == 0 else a*my_pow(a, n - 1)
  

def y(a, b, c):
  if c == 0 or a == 3:
    return math.inf
  return math.sin(2*a)/(a - 3) + math.atan(b)/c

def interpret(cmd):
  try: 
    a, b, c = [int(x) for x in cmd.split(' ')]
    return y(a, b, c)
  except Exception as e:
    handle(e)

def main():
  print("Enter 3 numbers separated by spaces\n\n")
  while True:
    try:
      cmd = input("lab5> ")
      if cmd.strip() != '':
        result = interpret(cmd)
        if result:
          print(result)
    
    except EOFError or KeyboardInterrupt:
      print('Bye!')
      exit(0)
    except Exception as e:
      handle(e)

if __name__ == "__main__":
  main()
