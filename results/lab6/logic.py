import math

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
