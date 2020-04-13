#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from inc.errorhandling import handle

def primes_lower_than(n):
  primes = []
  arr = list(range(2, n))
  for i in range(2, n):
    if 0 not in [i % x for x in primes]:
      primes.append(i)
  return [1] + primes

try:
  n = int(input('enter n> '))
  if n <= 0:
    raise ValueError('n must be greater than 0')
except Exception as e:
  handle(e)
  exit(0)

print(primes_lower_than(n))

