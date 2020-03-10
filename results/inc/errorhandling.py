import random
import os

ERROR_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__),"errors.txt"))
errors = []
with open(ERROR_FILE, 'r') as ef:
  for line in ef:
    errors.append(line.strip())
    
def handle(e: Exception):
  print(e)
  print(random.choice(errors))
