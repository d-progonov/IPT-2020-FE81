#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from results.inc.errorhandling import handle
import math

def vector_len(x, y, z):
  return math.sqrt(x*x + y*y + z*z)

def interpret(cmd):
  try:
    a, b, c = [float(x) for x in cmd.split(' ')]
    return vector_len(a, b, c)
  except Exception as e:
    handle(e)

def main():
  print("Enter three numbers (x, y, z) separated by spaces\n\n")
  while True:
    try:
      cmd = input("ex9> ").strip()
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
