class Location (object):
    def __init__(self, x, y):
        self.x = float(x) 
        self.y = float(y)

    def display(self):
        print("X is:", self.x)
        print("Y is:", self.y, '\n')


class Point (Location):
    def __init__(self, x, y):
        Location.__init__(self, x, y)

    def changePos(self, newX, newY):
        self.x = float(newX) 
        self.y = float(newY)
        print("New X is:", self.x)
        print("New Y is:", self.y)


class Line(Point):
    def __init__(self, x0, y0, length):
        Location.__init__(self, x0, y0)
        self.length = length

    def changePos(self, newX0, newY0):
        Point.changePos(self, newX0, newY0)

    def display(self):
        Location.display(self)
        print("Length is:", self.length)
        

class Circle(Point):
    def __init__(self, x0, y0, radius):
        Location.__init__(self, x0, y0)
        self.radius = abs(int(radius))

    def changeRadius(self, newR):
        self.radius = abs(int(newR))
        print("New radius is: ", self.radius, "\n")        

    def display(self):
        Location.display(self)
        print("Radius is:", self.radius)


class Square():
    def __init__(self, x0, y0, a, color):
        Location.__init__(self, x0, y0)
        self.a = abs(int(a))
        self.S = self.a**2
        self.c = str(color)


    def display(self):
        Location.display(self)
        print("S is:", self.S)
        print("Side is: ", self.a)
        print("Color is: ", self.S)

    def changeColor(self, newC):
        self.color = str(newC)
        print("New color is:", self.color, "\n")        


if __name__ == "__main__":
    print("Location object creating.")
    L = Location(10, 5)
    L.display()

    print("Point object creating.")
    P = Point(-10, 5)
    P.changePos(1, 1)
    P.display()

    print("Line object creating.")
    Ln = Line(2, 2, 10)
    Ln.changePos(1, 1)
    Ln.display()

    print("Circle object creating.")
    C = Circle(7, 7, 20)
    C.changePos(9, 9)
    C.changeRadius(30)
    C.display()

    print("Square object creating.")
    S = Square(4, 4, 10, "red")
    S.changeColor("green")
