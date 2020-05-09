#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from inc.errorhandling import handle
import numpy as np

# solve:
# ZI = E for I
# YE = J for E


# Part 1.
# Sleps:
# 1. Input n
# 2. Input Z-matrix
# 3. Input E-vector
# 4. Solve

def input_matrix(n, N):
  if n == 0:
    raise ValueError('n must be greater than 0!')
  ans = []
  for i in range(N):
    new_line = []
    l = 0
    while l != n:
      try:
        new_line = [int(x) for x in input('line ' + str(i + 1) + ': ').strip().split(' ')]
        l = len(new_line)
      except Exception as e:
        handle(e)
        continue
    ans.append(new_line)
  return ans

def print_solution(a_name, b_name, x_name):
  n = 0
  while n == 0:
    try:
      n = int(input("Enter n: "))
      if n < 0 or n > 7:
        raise ValueError('n must be greater than 0 and lower than 7!')
    except Exception as e:
      handle(e)
      n = 0
      continue

  print("Enter {}:".format(a_name))
  A = input_matrix(n, n)
  # print(Z)

  print("Enter {}:".format(b_name))
  B = [x[0] for x in input_matrix(1, n)]
  # print(E)

  print("Your result: ")
  A = np.array(A)
  B = np.array(B)
  X = np.linalg.solve(A, B)
  print(x_name + ': ' + repr(X))
  return 'Verified!' if np.allclose(np.dot(A, X), B) else 'Hmm...The matrix seems unsolvable'

def interpret(cmd):
  if cmd == 'nva':
    return print_solution('Z-matrix', 'E-vector', 'I')
  elif cmd == 'bcm':
    return print_solution('Y-matrix', 'J-vector', 'U')
  else:
    raise ValueError('Input either "BCM" or "NVA"')

def main():
  print("Do you want to use NVA (node voltage analysis) or BCM (branch current method)?\n\n")
  while True:
    try:
      cmd = input("lab10> ").strip()
      if cmd != '':
        result = interpret(cmd.lower())
        if result:
          print(result)
    
    except EOFError or KeyboardInterrupt:
      print('Bye!')
      exit(0)
    except Exception as e:
      handle(e)

if __name__ == "__main__":
  main()