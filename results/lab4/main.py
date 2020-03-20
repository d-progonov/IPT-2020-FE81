#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from inc.errorhandling import handle
import math
import random
from matrixtools import print_matrix, seq_matrix
import traceback

description = {
  'A': 'Enter integer n <Enter>. Then type in a sequence of numbers with length N \n \
        such that N = n^2 or \'default\' \n', 
  'B': 'Enter index of the element to delete in the list below:\n'
}

# Part B
identity = lambda x: x
even = lambda x: 0 if x % 2 == 0 else None

# Main
def interpret(cmd, part, *args):
  try:
    if cmd == '': return

    if cmd in [':A', ':B']:
      part = cmd[1]
      return description[part], part

    if part == 'A':
      n = int(cmd)
      N = n**2
      cmd = input('lab5:A:mode> ').strip()
      if cmd == 'default':
        seq = [_ for _ in range(0, N)]
      else:
        seq = [int(x) for x in cmd.split(' ')]
      
      m = seq_matrix(seq)
      print_matrix(m)
      return

    elif part == 'B':
      numbers = args[0]
      k = int(cmd)
      del numbers[k]
      print('Here is your list again, without kth element: {}'.format(numbers))
      print('Inserting zeroes after each even element...')

      return [f(x) for x in numbers for f in (identity, even) if f(x) is not None], part
    
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
      numbers = [random.randint(-100,100) for _ in range(random.randint(3, 30))]
      if part == 'B':
        print(numbers)

      result = interpret(
          input("lab5:{}> ".format(part)).strip(),
          part,
          numbers
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

