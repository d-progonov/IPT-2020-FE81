class TShape(object):
    def __init__(self, x, y):
        self.x = float(x) 
        self.y = float(y)

    def information(self):
        print("X is:", self.x)
        print("Y is:", self.y)

class TPoint(TShape):
    def __init__(self, x, y, c):
        self.x = float(x) 
        self.y = float(y)
        self.c = str(c)

    def changeColor(self, newC):
        self.c = newC
        print("New color is:", self.c, "\n")

    def information(self):
        TShape.information(self)
        print("Color is:", self.c)



class Ellipse(TPoint):
    def __init__(self, x0, y0, c):
        TPoint.__init__(self, x0, y0, c)

    def changePosition(self, newX, newY):
        self.x = newX
        self.y = newY
        print("New X is: ", self.x)
        print("New Y is: ", self.y, "\n")

    # Method changeColor() has already exist

    # Method information() has already exist


class Polygon(Ellipse): 
    def __init__(self, x0, y0, c, scale):
        Ellipse.__init__(self, x0, y0, c)
        self.scale = abs(int(scale))

    def changeScale(self, newS):
        self.scale = newS
        print("New scale is:", self.scale, "\n")

    def information(self):
        TPoint.information(self)
        print("Scale is:", self.scale)

    # Method changeColor() has already exist

    # Method changePosition() has already exist



class Sector(Ellipse):
    def __init__(self, x0, y0, brinkC, alpha):
        Ellipse.__init__(self, x0, y0, brinkC)
        self.alpha = abs(int(alpha))    

    def rotate(self, newAl):
        self.alpha = newAl  
        print("New alpha is:", self.alpha, "\n")

    def information(self):
        TPoint.information(self)
        print("Scale is:", self.alpha)

    # Method changeColor() has already exist

    # Method changePosition() has already exist

    # Method information() has already exist


if __name__ == "__main__":
    print("TShape object created.")
    S = TShape(1, 1)
    S.information()

    print("TPoint object created.")
    P = TPoint(2, 2, "Green")
    P.information()

    E = Ellipse(3, 3, "Red")
    E.changeColor("Black")
    E.changePosition(4, 4)
    E.information()

    Po = Polygon(5, 5, "White", 16)
    Po.changeScale(24)
    Po.information()

    Se = Sector(6, 6, "Yellow", 90)
    Se.rotate(180)
    Se.changeColor("Cyan")
    Se.changePosition(8, 8)
    Se.information()