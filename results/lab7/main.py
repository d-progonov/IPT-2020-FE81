#!/usr/bin/env python3
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from inc.errorhandling import handle, error_message

usage = 'main.py [input file]\n'

def main():
  try:
    if len(sys.argv) != 2:
      print(usage)
      return

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
      raise ValueError('Input file doesn\'t exist')
      return
  
    strings = []
    with open(input_file, 'r') as f:
      strings = [str(line).strip() for line in f]
    
    results = []
    first_line = strings.pop(0)
    for i, s in enumerate(strings):
      if first_line in s:
        s = ''.join(s.split(' '))
        results.append((i, s))

    print(results)

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
