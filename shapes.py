# shapes.py
class Position:
  def __init__(self, x = 0, y = 0):
    if x < 0:
      x = 0
    if y < 0:
      y = 0
    self.x = x
    self.y = y

  def cartesian(self):
      return [self.x, self.y]

  def __repr__(self):
    return 'position: x={0}, y={1}'.format(self.x, self.y)

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
    return 'color RBG: {0} {1} {2}'.format(self.red, self.green, self.blue)

class TShape:
  def __init__(self, position : Position = Position()):
    self.position = position

  def get_position(self):
    return self.position

  def set_position(self, p: Position):
    self.position = p

  def __repr__(self):
    return 'TShape <' + repr(self.position) + '>'

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
            str(self.get_size()))

class Ellipse(TPoint):
  def __init__(self, position : Position = Position(), size = 0, color : Color = Color()):
    super().__init__(position, size)
    self.color = color

  def get_color(self):
      return self.color

  def set_color(self, color : Color):
      self.color = color

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
      return 'Ellipse < {0} {1} size: {2} >'\
        .format(repr(self.get_position()), repr(self.get_color()), str(self.get_size()))

class Circle(Ellipse):
  def __init__(self, position : Position = Position(), size = 0,
    color : Color = Color(), fill: bool = False):
    super().__init__(position, size, color)
    self.fill = fill

  def get_fill(self):
      return self.fill

  def set_fill(self, fill: bool):
      self.fill = fill

  def __repr__(self):
    return 'Circle < {0} {1} size: {2} fill: {3} >'\
        .format(repr(self.get_position()), repr(self.get_color()),
            str(self.get_size()), self.fill)

class SectorAngle:
  def __init__(self, startAngle: int = 0, endAngle: int = 0):
      if startAngle < 0:
        startAngle = 0
      elif startAngle > 360:
        startAngle = 360

      if endAngle < 0:
        endAngle = 0
      elif endAngle > 360:
        endAngle = 360

      if endAngle > startAngle:
          self.startAngle = startAngle
          self.endAngle = endAngle
      else:
          self.startAngle = endAngle
          self.endAngle = startAngle

  def get_angles(self):
      return [self.startAngle, self.endAngle]

  def set_angles(self, startAngle: int, endAngle: int):
      self.startAngle = startAngle
      self.endAngle = endAngle

  def __repr__(self):
    return 'Angle < {0} {1} >'\
        .format(str(self.startAngle), str(self.endAngle))

class Sector(Ellipse):
  def __init__(self, position : Position = Position(), size = 0,
    color : Color = Color(), fill: bool = False, angle: SectorAngle = SectorAngle()):
    super().__init__(position, size, color)
    self.fill = fill
    self.angle = angle

  def get_fill(self):
      return self.fill

  def set_fill(self, fill: bool):
      self.fill = fill

  def get_angle(self):
      return self.angle

  def set_angle(self, angle: SectorAngle):
      self.angle = angle

  def __repr__(self):
    return 'Sector < {0} {1} size: {2} fill: {3} angle: {4} >'\
        .format(repr(self.get_position()), repr(self.get_color()),
            str(self.get_size()), self.fill, repr(self.get_angle()))
