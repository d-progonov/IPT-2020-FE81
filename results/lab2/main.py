#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from inc.errorhandling import handle
import math

def sign(number):
  if float(number) == 0:
    return '0'
  return ('+' if float(number) > 0 else '-')

def interpret(cmd):
  try:
    return sign(cmd)
  except Exception as e:
    handle(e)

def main():
  print("Enter a number\n\n")
  while True:
    try:
      cmd = input("lab2> ").strip()
      if cmd != '':
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
