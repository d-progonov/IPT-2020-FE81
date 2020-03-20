import math
# Part A
def is_first_line(position, n):
  return position < n

def is_last_line(position, n):
  return position >= n*(n - 1)

def is_first_column(position, n):
  return position % n == 0

def is_last_column(position, n):
  return (position + 1) % n == 0

def is_last(position, n):
  return position == n*n - 1

def move_down(position, n):
  return position + n

def move_right(position, n):
  return position + 1

def move_NW(position, n):
  return position - (n - 1)

def move_SE(position, n):
  return position + (n - 1)

def make_matrix(lst, n):
  ans = []
  while lst != []:
    ans += [lst[:n]]
    lst = lst[n:]
  return ans

def seq_matrix(sequence):
  N = len(sequence)
  if N == 0: return
  if N == 1: return sequence

  n = int(math.sqrt(N))
  position = 0
  ans = [None]*N

  while position < N:
    ans[position] = sequence.pop()
    if not is_last_line(position, n):
      position = move_down(position, n)
    elif not is_last(position, n):
      position = move_right(position, n)
    
    while not is_first_line(position, n) and not is_last_column(position, n):
      ans[position] = sequence.pop() 
      position = move_NW(position, n)

    if not is_last(position, n):
      ans[position] = sequence.pop()
    if not is_last_column(position, n):
      position = move_right(position, n)
    else:
      position = move_down(position, n)
    
    while not is_first_column(position, n) and not is_last_line(position, n):
      ans[position] = sequence.pop()
      position = move_SE(position, n)
    
  return make_matrix(ans, n)

def print_matrix(matrix):
  s = [[str(e) for e in row] for row in matrix]
  lens = [max(map(len, col)) for col in zip(*s)]
  fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
  table = [fmt.format(*row) for row in s]
  print('\n'.join(table))