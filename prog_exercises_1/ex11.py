#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from results.inc.errorhandling import handle
import math

def good(l, d, h, a, b):
  brick_params = [l, d, h]
  S = a*b
  x = min(brick_params)
  brick_params.remove(x)
  y = min(brick_params)
  return x*y <= S

def interpret(cmd):
  try:
    l, d, h, a, b = [int(x) for x in cmd.split(' ')]
    return 'пролезет' if good(l, d, h, a, b) else 'не пролезет'
  except Exception as e:
    handle(e)

def main():
  print("Enter five numbers (l, d, h, a, b) separated by spaces\n\n")
  while True:
    try:
      cmd = input("ex11> ").strip()
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
