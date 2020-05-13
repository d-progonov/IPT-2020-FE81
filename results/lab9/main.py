import sys, os
from shapes_c import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from inc.errorhandling import handle

ids = {
  # 'id': obj,
}

shapes = {
  'TShape': TShape,
  'TPoint': TPoint, 
  'Polygon': Polygon,
  'Ellipse': Ellipse,
  'Ring': Ring,
  'Sector': Sector
}

def print_help():
  print('Command help:')
  print('\t[list    / l]')
  print('\t[create  / c] <type> [<n>]')
  print('\t[delete  / d] <id>')
  print('\t[inspect / i] <id>')
  print('\t[move    / m] <id> <x> <y>')
  print('\t[paint   / p] <id> <R> <G> <B>')
  print('\t[scale   / s] <id> <size>')
  print('Available types:')
  print(str([s + '\n' for s in shapes.keys()]))
  print ("""
  Example:
      > list
      >>> ...
      > create TPoint
      >>> Created new TPoint with id 9982
      > move 9982 20 30
      > inspect 9982
      >>> TPoint <20, 30>
      > paint 9982 255 255 255
      >>> This shape does not support this method!
  """)

def list_obj():
  return '\n'.join(['{0}:{1}'.format(k, v) for k, v in ids.items()])

def create_obj(obj, n):
  ans = []
  if n <= 0:
    raise ValueError('n must be greater than 1!')
  if obj not in shapes.keys():
    raise ValueError('Incorrect object name')
  base = len(ids)
  for i, _ in enumerate(range(n)):
    ids[str(i + base)] = shapes[obj]()
    ans.append('Created new ' + obj + ' with id ' + str(i+base))
  return '\n'.join(ans)

def move_obj(id, x, y):
  ids[id].set_position(Position(x, y))
  return 'New position for ' + id + ': ' + repr(ids[id].get_position())

def paint_obj(id, clr):
  r, g, b = [x if x in range(255) else 0 for x in clr]
  c = Color(r, g, b)
  ids[id].set_color(c)
  return 'Painted {0} with id {1} to color {2}'.format(repr(ids[id]), id, c)

def delete_obj(id : str):
  if int(id) not in range(len(ids) - 1):
    raise IndexError
  ids.pop(id)
  return 'Removed object with id ' + id

def scale_obj(id, size):
  ids[id].set_size(size)
  return 'The size of object ' + id + ' was succesfully changed!'

def inspect_obj(id):
  return repr(ids[id])

def interpret(cmd):
  try:
    action, *params = cmd.split(' ')
    obj = params.pop(0) if len(params) != 0 else None

    if action in ['c', 'create']:
      if len(params) == 0:
        params = [1]
      return create_obj(obj, int(params[0]))
    elif action in ['d', 'delete']:
      return delete_obj(obj)
    elif action in ['m', 'move']:
      x, y = [int(x) for x in params]
      return move_obj(obj, x, y)
    elif action in ['i', 'inspect']:
      return inspect_obj(obj)
    elif action in ['l', 'list']:
      return list_obj()
    elif action in ['p', 'paint']:
      if len(params) == 0:
        params = ['0', '0', '0']
      return paint_obj(obj, (int(c) for c in params))
    elif action in ['s', 'scale']:
      return scale_obj(obj, int(params[0]))
    else:
      raise ValueError('Incorrect keyword')
  except Exception as e:
    handle(e)

def main():
  print_help()
  create_obj('TPoint', 40)
  print(list_obj())
  while True:
    try:
      cmd = input("lab9> ").strip()
      if cmd != '':
        result = interpret(cmd)
        if result:
          print(result)
    
    except EOFError or KeyboardInterrupt:
      print('Bye!')
      exit(0)
    except Exception as e:
      handle(e)

if __name__ == '__main__':
  main()
  