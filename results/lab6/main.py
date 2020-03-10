#!/usr/bin/env python3
import sys, os, re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from inc.errorhandling import handle, error_message
from logic import f, my_pow

description = {
  'A': 'Enter two numbers (s and t)\n', 
  'B': 'Enter two numbers (a and n)\n',
  'Usage': 'main.py [input file] [output file]\n\
  [input file] format:\n\
  \tmode: ...args\n\
  Example: input.txt\n\
  \tA: 1 2\n\
  \tB: 3 4\n\
  \tA: 0 0\n\
  \t...\n'
}

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
  if len(sys.argv) != 3:
    print(description['Usage'])
    return

  del sys.argv[0]
  input_file, output_file = sys.argv

  if not os.path.exists(input_file):
    handle(ValueError('Input file doesn\'t exist'))
    return

  try:
    results = []
    with open(input_file, 'r') as data_file:
      for line in data_file:
        options = re.search(r'^(A|B): (\d \d)$', line.strip(), flags=0)
        if not options: 
          results.append(error_message())
          continue
        
        part = options.group(1)
        cmd = options.group(2)
        result = interpret(cmd, part)
        
        if result:
          message, part = result
          results.append(message)

    with open(output_file, 'w') as f:
        f.writelines([str(str(s) + '\n') for s in results])

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
