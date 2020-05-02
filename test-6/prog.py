class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
      
  def insert(self, child):
    if child.val > self.val:
      if self.right is None:
        self.right = child
      else:
        self.right.insert(child)
    else:
      if self.left is None:
        self.left = child
      else:
        self.left.insert(child)





   
    