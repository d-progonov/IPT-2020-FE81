#!/usr/bin/env python3
import random
import os

ERROR_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__),"errors.txt"))
errors = []
with open(ERROR_FILE, 'r') as ef:
  for line in ef:
    errors.append(line.strip())

def error_message():
  return random.choice(errors) 

def handle(e: Exception):
  print(e)
  print(error_message())
