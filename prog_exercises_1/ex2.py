#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from results.inc.errorhandling import handle
import math

def y(a, b, f):
  if a == 0:
    return math.inf
  return (a + b - f / a) + f * a * a - (a + b)

def interpret(cmd):
  try: 
    a, b, f = [float(x) for x in cmd.split(' ')]
    return y(a, b, f)
  except Exception as e:
    handle(e)

def main():
  print('Expression Calculator')
  print('\t(a + b - f / a) + f * a * a - (a + b)')
  print("Enter 3 numbers (a b f) separated by spaces\n\n")
  while True:
    try:
      cmd = input("ex2> ").strip()
      if cmd != '':
        result = interpret(cmd)
        if result is not None:
          print(result)
    
    except EOFError or KeyboardInterrupt:
      print('Bye!')
      exit(0)
    except Exception as e:
      handle(e)

if __name__ == "__main__":
  main()
