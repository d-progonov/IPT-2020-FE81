def Manual():
    print("- - Input data manual - - ")
    print("   See inputing rules: ")
    print("     - Float data: coordinates;")
    print("     - String data: colors;")
    print("     - Integer data: radii, lengths, sizes.")
    print("   Class hierarchy of signatures:")
    print("     - TShape(xpos, ypos)")
    print("     - TPoint(xpos, ypos)")
    print("     - TCircle(x0pos, y0pos, radius)")
    print("     - TEllipse(x0pos, y0pos, a_side, b_side, color)")
    print("     - TSector(x0pos, y0pos, radius, angle, color)", "\n")



class TShape(object):
    def __init__(self, x, y):
        self.x = float(x) 
        self.y = float(y)
        print("TShape Object.")

    def display(self):
        print("X is:", self.x)
        print("Y is:", self.y)


class TPoint(TShape):
    def __init__(self, x, y):
        self.x = float(x) 
        self.y = float(y)
        self.N = 40
        print("TPoint Objects.")

    def display(self):
        TShape.display(self)
        print("Number of points: ", self.N, "\n")


class TCircle(TPoint):
    def __init__(self, x0, y0, r):
        self.x = float(x0) 
        self.y = float(y0)
        self.R = int(r)
        print("TCircle Objects.")

    def display(self):
        TShape.display(self)
        print("Radius is: ", self.R, "\n")

    def changeSize(self, newR):
        self.R = int(newR)
        print("New radius is: ", self.R)

    def changeCenter(self, newX, newY):
        self.x = float(newX) 
        self.y = float(newY)
        print("Center coordinates has changes.")

    #  Method display() is here too  # 


class TEllipse(TCircle):
    def __init__(self, x0, y0, a, b, color):
        self.x = float(x0) 
        self.y = float(y0)
        self.a = int(a)
        self.b = int(b)
        self.c = str(color)
        print("TEllipse Objects.")

    def display(self):
        TShape.display(self)
        print("Major is: ", self.a)
        print("Minor is: ", self.b)
        print("Color is: ", self.c, "\n")

    def changeSize(self, new_a, new_b):
        self.a = int(new_a)
        self.b = int(new_b)
        print("New major and minor is: ")
        print("A: ", self.a)
        print("B: ", self.b)

    #  Method changeCenter is here too  # 


class TSector(TEllipse):
    def __init__(self, x0, y0, r, angle, color):
        self.x = float(x0) 
        self.y = float(y0)
        self.R = int(r)
        self.angle = int(angle)

        self.S = float((self.angle/2) * (self.R)**2)
        self.c = str(color)
        print("TSector Objects.")
    
    def display(self):
        TShape.display(self)
        print("R is ", self.R)
        print("S is: ", self.S)
        print("Angle is: ", self.angle)
        print("Color is: ", self.c, "\n")

    def changeColor(self, newC):
        self.c = str(newC)
        print("New color is: ", self.c)

    def changeShape(self, newAn):
        self.angle = int(newAn)
        print("New color is: ", self.angle)

    

if __name__ == "__main__":
    try:
        # Manual()

        S = TShape(2, 1)
        S.display()
        print("\n")
        P = TPoint(2, 2)
        P.display()
        print("\n")
        C = TCircle(3, 3, 10)
        C.changeCenter(4, 4)
        C.changeSize(20)
        C.display()
        print("\n")
        E = TEllipse(5, 5, 8, 4, "Red")
        E.changeCenter(-1, -1)
        E.changeSize(9, 2)
        E.display()
        print("\n")
        Se = TSector(9, 9, 10, 90, "Black")
        Se.changeCenter(-6, -5)
        Se.changeShape(180)
        Se.changeColor("Yellow")
        Se.display()
        print("\n")
        
    except ValueError():
        Manual()