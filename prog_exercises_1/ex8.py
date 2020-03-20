#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from results.inc.errorhandling import handle
import math

def my_pow(N, k):
  x = 1
  for _ in range(k):
    x *= N
  return x

def interpret(cmd):
  try:
    N, k = [int(x) for x in cmd.split(' ')]
    return my_pow(N, k)
  except Exception as e:
    handle(e)

def main():
  print("Enter two numbers separated by spaces\n\n")
  while True:
    try:
      cmd = input("ex8> ").strip()
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
