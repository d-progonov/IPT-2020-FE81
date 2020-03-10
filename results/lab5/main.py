#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from inc.errorhandling import handle
import math

description = {
  'A': 'Enter two numbers (s and t)\n', 
  'B': 'Enter two numbers (a and n)\n'
}

# Part A
def f(a, b, c = 1.17):
  return (2*a - b - math.sin(c))/(5 + abs(c))

# Part B
def my_pow(a, n):
  if a == 0:
    raise ValueError("base number must be non-zero")
  if n < 0:
    raise ValueError("power must be non-negative")
  return 1 if n == 0 else a*my_pow(a, n - 1)

# Main
def interpret(cmd, part):
  try:
    if cmd == '': return

    if cmd in [':A', ':B']:
      part = cmd[1]
      return description[part], part

    if part == 'A':
      s, t = [float(x) for x in cmd.split(' ')]
      return f(t, -2*s) - f(2.2, t, s - t), part

    elif part == 'B':
      a, n = [float(x) for x in cmd.split(' ')]
      n = int (n)
      return my_pow(a, n), part
    
    else:
      raise ValueError("Part must be either A or B")
  except Exception as e:
    handle(e)

def main():
  print("To switch between task spaces, type :A or :B\n")
  part = 'A'
  print(description[part])

  while True:
    try:
      result = interpret(
          input("lab5:{}> ".format(part)).strip(),
          part
        )
      
      if result:
        message, part = result
        print(message)

    except KeyboardInterrupt:
      print('Bye!')
      exit(0)
    except Exception as e:
      if e.__class__ == EOFError:
        print('Bye!')
        exit(0)
      handle(e)

if __name__ == "__main__":
  main()
