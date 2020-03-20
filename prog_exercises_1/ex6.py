#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from results.inc.errorhandling import handle
import math

def interpret(cmd):
  try:
    N, k = [int(x) for x in cmd.split(' ')]
    return sum([x**k for x in range(1, N + 1)])
  except Exception as e:
    handle(e)

def main():
  print("Enter two numbers separated by spaces\n\n")
  while True:
    try:
      cmd = input("ex6> ").strip()
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
