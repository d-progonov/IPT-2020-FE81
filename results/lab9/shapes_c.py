class Position:
  def __init__(self, x = 0, y = 0):
    if x < 0:
      x = 0
    if y < 0:
      y = 0
    self.x = x
    self.y = y

  def __repr__(self):
    return ' pos: ({0}, {1}) '.format(self.x, self.y)


class Color:
  def __init__(self, red = 0, green = 0, blue = 0):
    self.red = red
    self.green = green
    self.blue = blue

  def setRGB(self, r, g, b):
    self.red, self.green, self.blue = r, g, b

  @classmethod
  def from_hex(cls, hex):
    c = cls()
    c.red, c.green, c.blue = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    return c

  def __repr__(self):
    return ' color: {0} {1} {2} '.format(self.red, self.green, self.blue)


class TShape:
  def __init__(self, position : Position = Position()):
    self.position = position

  def get_position(self):
    return self.position

  def set_position(self, p: Position):
    self.position = p
  
  def __repr__(self):
    return 'TShape <' + repr(self.position) + '>'
  
  def paint(self):
    return 'This shape does not support this method!'


class TPoint(TShape):
  def __init__(self, position : Position = Position(), size = 0):
    super().__init__(position)
    self.size = size

  def get_size(self):
    return self.size

  def set_size(self, size):
    self.size = abs(size)

  def get_position(self):
    return super().get_position()
  
  def set_position(self, p):
    return super().set_position(p)

  def __repr__(self):
    return 'TPoint < {0} size: {1} >'\
    .format(repr(self.get_position()), 
            str(self.get_size())
    )

class Polygon(TPoint):
  def __init__(self, position : Position = Position(), size = 0, color : Color = Color()):
    super().__init__(position, size)
    self.color = color

  def get_color(self):
    return self.color

  def set_color(self, color : Color):
    self.color = color

  def __repr__(self):
    return 'Polygon < {0} size: {1} {2} >'\
    .format(repr(self.get_position()), 
            str(self.get_size()), 
            repr(self.get_color())
    )
  

class Ellipse(TPoint):
  def __init__(self, position : Position = Position(), size = 0):
    super().__init__(position, size)
  
  def move(self, side, distance):
    x, y = self.position.cartesian()
    if side == 'up':
      y += distance
    elif side == 'down':
      y -= distance
    elif side == 'left':
      x -= distance
    elif side == 'right':
      x += distance
    
    self.position = Position(x, y)

  def __repr__(self):
    return 'Ellipse <' + repr(self.get_position()) + \
           str(self.get_size()) + '>'
  
class Ring(Ellipse):
  def __init__(self, position : Position = Position(), size = 0, color : Color = Color()):
    super().__init__(position, size)
    self.color = color

  def get_color(self):
    return self.color

  def set_color(self, color : Color):
    self.color = color

  def __repr__(self):
    return 'Ring <' + repr(self.get_position()) + \
           str(self.get_size()) + repr(self.get_color()) + '>'

class Sector(Ellipse):
  def __init__(self, position : Position = Position(), size = 0, color : Color = Color()):
    super().__init__(position, size)
    self.color = color
  
  def get_color(self):
    return self.color

  def set_color(self, color : Color):
    self.color = color

  def __repr__(self):
    return 'Ellipse <' + repr(self.get_position()) + \
           str(self.get_size()) + repr(self.get_color()) + '>'
