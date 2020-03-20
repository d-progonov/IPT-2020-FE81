#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from results.inc.errorhandling import handle
import math

def print_triangle(n):
  print('+')
  for i in range(1, n-1):
    print('+{}+'.format(' '*i))
  print('+ ' * (int(n/2) + 1) + '+'*(n % 2))
def interpret(cmd):
  try:
    print_triangle(int(cmd))
  except Exception as e:
    handle(e)

def main():
  print("Enter triangle side length\n\n")
  while True:
    try:
      cmd = input("ex3> ").strip()
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
