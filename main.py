# main.py
import sys, os
from shapes import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

shapes = {
  'TShape': TShape,
  'TPoint': TPoint,
  'Ellipse': Ellipse,
  'Circle': Circle,
  'Sector': Sector
}

def main():
  print('Available types:')
  print(str([s + ' ' for s in shapes.keys()]))
  circle = Circle(Position(5, 50), 50, Color(20, 20, 20), True)
  print(repr(circle))
  print('Moving up by 20')
  circle.move('up', 20)
  print(repr(circle))
  print('Changing fill to False')
  circle.set_fill(False)
  print(repr(circle))


  sector = Sector(Position(20, 10), 30, Color(2, 2, 2), True,
    SectorAngle(90, 270))
  print(repr(sector))
  print('Changing color to rbg 50 50 50')
  sector.set_color(Color(50, 50, 50))
  print(repr(sector))
  print('Changing angle to 180-360')
  sector.set_angle(SectorAngle(180, 360))
  print(repr(sector))

if __name__ == '__main__':
  main()
