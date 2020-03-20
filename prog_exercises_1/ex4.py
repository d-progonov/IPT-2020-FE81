#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from results.inc.errorhandling import handle
import math

def interpret(cmd):
  try:
    a, b = [float(x) for x in cmd.split(' ')]
    message = ''
    if a > b:
      message = 'больше'
    elif a < b:
      message = 'меньше'
    else:
      message = 'Эти числа равны'
    return message
  except Exception as e:
    handle(e)

def main():
  print("Enter two numbers separated by spaces\n\n")
  while True:
    try:
      cmd = input("ex4> ").strip()
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
