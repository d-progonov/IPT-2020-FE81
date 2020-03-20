#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from results.inc.errorhandling import handle
import math

def interpret(cmd):
  try:
    n = int(cmd)
    if n < 0:
      raise ValueError('N должно быть натуральным')
    n = [int(x) for x in list(n)]
    if len(n) != 2:
      raise ValueError('число должно иметь 2 цифры')
    return 'max: {0} min: {1}'.format(max(n), min(n))
  except Exception as e:
    handle(e)

def main():
  print("Enter a two-digit number separated by spaces\n\n")
  while True:
    try:
      cmd = input("ex7> ").strip()
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
