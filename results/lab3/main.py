#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from inc.errorhandling import handle
import math


def a(i):
  return pow(-1, i-1)/pow(i, i)

def main():
  EPSILON = pow(10, -4)
  try:
    a_sum = 0
    i = 0
    while True:
      curr = a(i)
      if abs(curr) <= EPSILON:
        break
      a_sum += curr
      i += 1

    print("a_({0}): {1}".format(i + 1, a_sum))
  except Exception as e:
    handle(e)

if __name__ == "__main__":
  main()
