class TShape(object):
    ins = []

    def __new__(cls, *args, **kwargs):
        ins = object.__new__(cls)
        cls.ins.append(ins)
        return ins
    def __init__(self, color="green", width=1, heigh=1):
        self.color = color
        self.width = width
        self.heigh = heigh

    def __del__(self):
        try:
            self.ins.remove(self)
        except ValueError:
            pass


class Pixel(TShape):
    ins = []

    def __new__(cls, *args, **kwargs):
        if len(cls.ins)==20:
            print("There is no more space for new objects")
        else:
            ins = object.__new__(cls)
            cls.ins.append(ins)
            return ins
    def __init__(self, color, width=1, heigh=1):
        TShape.__init__(self, color, width, heigh)
    def change_color(self, color):
        self.color = color

class Circle(Pixel):
    ins = []
    def __init__(self, color, radius,transparency=1, is_rotating=0, width=1, heigh=1):
       Pixel.__init__(self, color, 2*radius, 2*radius)
       self.radius = radius
       self.transparency = transparency
       self.is_rotating = is_rotating
    def change_color(self, color, transparency):
        self.color = color
        self.transparency = transparency
    def moving(self):
        if self.is_rotating == 0:
            print("Object is not rotating. Start rotating... Object is rotating now.")
            self.is_rotating=1
        else:            
            print("Object is rotating. Stop rotating... Object is not rotating now.")
            self.is_rotating=0
    def change_radius(self, radius):
        self.radius=radius

class Square(Pixel):
    ins = []
    def __init__(self, color, width=1, contrast=1, is_rolling=0):
           Pixel.__init__(self, color, width, width )
           self.contrast = contrast
           self.is_rolling = is_rolling
    def change_color(self, color, contrast):
        self.color = color
        self.contrast = contrast
    def moving(self):
        if self.is_rolling == 0:
            print("Object is not rolling. Start rolling... Object is rolling now.")
            self.is_rolling=1
        else:            
            print("Object is rolling. Stop rolling... Object is not rolling now.")
            self.is_rolling=0
    def change_size(self, width):
        self.width = width
        self.heigh = width

class Rectangle(Square):
    ins = []
    def __init__(self, color, width=1,heigh=1, contrast=1, brightness=1, is_rolling=0, is_jumping=0):
           Pixel.__init__(self, color, width, heigh )
           self.contrast = contrast
           self.brightness = brightness
           self.is_rolling = is_rolling
           self.is_jumping = is_jumping
    def change_color(self, color, contrast, brightness):
        self.color = color
        self.contrast = contrast
        self.brightness = brightness
    def moving(self):
        if (self.is_rolling == 0)and(self.is_jumping == 0):
            print("Object is not rolling and not jumping. Start rolling and jumping... Object is rolling and jumping now.")
            self.is_rolling=1
            self.is_jumping=1
        else:            
            print("Object is rolling and jumping. Stop rolling and jumping... Object is not rolling and not jumping now.")
            self.is_rolling=0
            self.is_jumping=0
    def change_size(self, width, heigh):
        self.width = width
        self.heigh = heigh


def TShapef():
    while(True):
        print("Choose acting:", "1 - create new one", "2 - delete last one", "3 - get amount of objects", "4 - go out")
        try:
            a=int(input())
            if (a<1)or(a>4):
                raise Exception
        except Exception:
            print("Choose from list, please")
            a = -1
        if a==1:
            ins = TShape()
        elif a==2:
            if len(TShape.ins)==0:
                print("There is nothing to delete")
            else:
                TShape.ins[-1].__del__()
        elif a==3:
            print("Amount of objects:", len(TShape.ins))
        else:
            break

def Pixelf():
    while(True):
        print("Choose acting:", "1 - create new one", "2 - delete last one", "3 - get amount of objects", "4 - change color of last one", "5 - get color of last one","6 - go out")
        try:
            a=int(input())
            if (a<1)or(a>6):
                raise Exception
        except Exception:
            print("Choose from list, please")
            a = -1
        if a==1:
               color=str(input("Enter color ="))
               ins = Pixel(color)
        elif a==2:
            if len(Pixel.ins)==0:
                print("There is nothing to delete")
            else:
                Pixel.ins[len(Pixel.ins)-1].__del__()
        elif a==3:
            print("Amount of objects:", len(Pixel.ins))
        elif a==4:
            if len(Pixel.ins)==0:
                print("There is no object")
            else:
                while(1):
                    try:
                        color=str(input("Enter new color ="))
                        break
                    except Exception:
                        print("Wrong data type of variable")
                Pixel.ins[len(Pixel.ins)-1].change_color(color)
        elif a==5:
            if len(Pixel.ins)==0:
                print("There is no object")
            else:
                print("Color of last one:",Pixel.ins[len(Pixel.ins)-1].color)
        else:
            break

def Circlef():
    while(True):
        print("Choose acting:", "1 - create new one", "2 - delete last one", "3 - get amount of objects", "4 - change color of last one", "5 - get color of last one","6 - change transparency of last one", "7 - get transparency of last one","8 - start/stop rotating","9 - change radius","10 - get radius","11 - go out")
        try:
            a=int(input())
            if (a<1)or(a>11):
                raise Exception
        except Exception:
            print("Choose from list, please")
            a = -1
        if a==1:
            while(True):
                try:
                    color=str(input("Enter color ="))
                    radius=float(input("Enter radius ="))
                    transparency=float(input("Enter transparency ="))
                    if (radius<=0)or(transparency<=0):
                        raise Exception
                    break
                except Exception:
                    print("Wrong data of variable(s)")
            ins = Circle(color,radius,transparency)
        elif a==2:
            if len(Circle.ins)==0:
                print("There is nothing to delete")
            else:
                Circle.ins[len(Circle.ins)-1].__del__()
        elif a==3:
            print("Amount of objects:", len(Circle.ins))
        elif a==4:
            if len(Circle.ins)==0:
                print("There is no object")
            else:
                while(1):
                    try:
                        color=str(input("Enter new color ="))
                        break
                    except Exception:
                        print("Wrong data type of variable")
                Circle.ins[len(Circle.ins)-1].change_color(color, Circle.ins[len(Circle.ins)-1].transparency)
        elif a==5:
            if len(Circle.ins)==0:
                print("There is no object")
            else:
                print("Color of last one:",Circle.ins[len(Circle.ins)-1].color)
        elif a==6:
            if len(Circle.ins)==0:
                print("There is no object")
            else:
                while(1):
                    try:
                        transparency=float(input("Enter new transparency ="))
                        if (transparency<=0):
                            raise Exception
                        break
                    except Exception:
                        print("Wrong data type of variable")
                Circle.ins[len(Circle.ins)-1].change_color(Circle.ins[len(Circle.ins)-1].color, transparency)
        elif a==7:
            if len(Circle.ins)==0:
                print("There is no object")
            else:
                print("Transparency of last one:",Circle.ins[len(Circle.ins)-1].transparency)
        elif a==8:
            if len(Circle.ins)==0:
                print("There is no object")
            else:
                Circle.ins[len(Circle.ins)-1].moving()  
        elif a==9:
            if len(Circle.ins)==0:
                print("There is no object")
            else:
                while(1):
                    try:
                        radius=float(input("Enter new radius ="))
                        if (radius<=0):
                            raise Exception
                        break
                    except Exception:
                        print("Wrong data type of variable")
                Circle.ins[-1].change_radius(radius)
        elif a==10:
            if len(Circle.ins)==0:
                print("There is no object")
            else:
                print("Radius of last one:",Circle.ins[-1].radius)
        else:
            break

def Squaref():
    while(True):
        print("Choose acting:", "1 - create new one", "2 - delete last one", "3 - get amount of objects", "4 - change color of last one", "5 - get color of last one","6 - change contrast of last one", "7 - get contrast of last one","8 - change size of last one","9 - get size of last one","10 - start/stop rolling","11 - go out")
        try:
            a=int(input())
            if (a<1)or(a>11):
                raise Exception
        except Exception:
            print("Choose from list, please")
            a = -1
        if a==1:
            while(True):
                try:
                    color=str(input("Enter color ="))
                    size=float(input("Enter size(width) ="))
                    contrast=float(input("Enter contrast ="))
                    if (size<=0)or(contrast<=0):
                        raise Exception
                    break
                except Exception:
                    print("Wrong data of variable(s)")
            ins = Square(color, size, contrast)
        elif a==2:
            if len(Square.ins)==0:
                print("There is nothing to delete")
            else:
               Square.ins[len(Square.ins)-1].__del__()
        elif a==3:
            print("Amount of objects:", len(Square.ins))
        elif a==4:
            if len(Square.ins)==0:
                print("There is no object")
            else:
                while(1):
                    try:
                        color=str(input("Enter new color ="))
                        break
                    except Exception:
                        print("Wrong data of variable")
                Square.ins[len(Square.ins)-1].change_color(color,Square.ins[len(Square.ins)-1].contrast)
        elif a==5:
            if len(Square.ins)==0:
                print("There is no object")
            else:
                print("Color of last one:",Square.ins[len(Square.ins)-1].color)
        elif a==6:
            if len(Square.ins)==0:
                print("There is no object")
            else:
                while(1):
                    try:
                        contrast=float(input("Enter new contrast ="))
                        if (contrast<=0):
                            raise Exception
                        break
                    except Exception:
                        print("Wrong data of variable")
                Square.ins[len(Square.ins)-1].change_color(Square.ins[len(Square.ins)-1].color, contrast)
        elif a==7:
            if len(Square.ins)==0:
                print("There is no object")
            else:
                print("Contrast of last one:",Square.ins[len(Square.ins)-1].contrast)
        elif a==8:
            if len(Square.ins)==0:
                print("There is no object")
            else:
                while(1):
                    try:
                        size=float(input("Enter new size(width) ="))
                        if (size<=0):
                            raise Exception
                        break
                    except Exception:
                        print("Wrong data of variable")
                Square.ins[len(Square.ins)-1].change_size(size)
        elif a==9:
            if len(Square.ins)==0:
                print("There is no object")
            else:
                print("Size of last one:",Square.ins[len(Square.ins)-1].width)
        elif a==10:
            if len(Square.ins)==0:
                print("There is no object")
            else:
                Square.ins[len(Square.ins)-1].moving()  
        else:
            break

def Rectanglef():
    while(True):
        print("Choose acting:", "1 - create new one", "2 - delete last one", "3 - get amount of objects", "4 - change color of last one", "5 - get color of last one","6 - change contrast of last one", "7 - get contrast of last one","8 - change brightness of last one", "9 - get brightness of last one","10 - change size of last one","11 - get size of last one","12 - start/stop moving","13 - go out")
        try:
            a=int(input())
            if (a<1)or(a>13):
                raise Exception
        except Exception:
            print("Choose from list, please")
            a = -1
        if a==1:
            while(True):
                try:
                    color=str(input("Enter color ="))
                    width=float(input("Enter width ="))
                    heigh=float(input("Enter heigh ="))
                    contrast=float(input("Enter contrast ="))
                    brightness=float(input("Enter brightness ="))
                    if (brightness<=0)or(contrast<=0)or(width<=0)or(heigh<=0):
                        raise Exception
                    break
                except Exception:
                    print("Wrong data of variable(s)")
            ins = Rectangle(color,width,heigh,contrast,brightness)
        elif a==2:
            if len(Rectangle.ins)==0:
                print("There is nothing to delete")
            else:
               Rectangle.ins[len(Rectangle.ins)-1].__del__()
        elif a==3:
            print("Amount of objects:", len(Rectangle.ins))
        elif a==4:
            if len(Rectangle.ins)==0:
                print("There is no object")
            else:
                while(1):
                    try:
                        color=str(input("Enter new color ="))
                        break
                    except Exception:
                        print("Wrong data of variable")
                Rectangle.ins[len(Rectangle.ins)-1].change_color(color,Rectangle.ins[len(Rectangle.ins)-1].contrast,Rectangle.ins[len(Rectangle.ins)-1].brightness)
        elif a==5:
            if len(Rectangle.ins)==0:
                print("There is no object")
            else:
                print("Color of last one:",Rectangle.ins[len(Rectangle.ins)-1].color)
        elif a==6:
            if len(Rectangle.ins)==0:
                print("There is no object")
            else:
                while(1):
                    try:
                        contrast=float(input("Enter new contrast ="))
                        if (contrast<=0):
                            raise Exception
                        break
                    except Exception:
                        print("Wrong data of variable")
                Rectangle.ins[len(Rectangle.ins)-1].change_color(Rectangle.ins[len(Rectangle.ins)-1].color, contrast,Rectangle.ins[len(Rectangle.ins)-1].brightness)
        elif a==7:
            if len(Rectangle.ins)==0:
                print("There is no object")
            else:
                print("Contrast of last one:",Rectangle.ins[len(Rectangle.ins)-1].contrast)
        elif a==8:
            if len(Rectangle.ins)==0:
                print("There is no object")
            else:
                while(1):
                    try:
                        brightness=float(input("Enter new brightness ="))
                        if (brightness<=0):
                            raise Exception
                        break
                    except Exception:
                        print("Wrong data of variable")
                Rectangle.ins[len(Rectangle.ins)-1].change_color(Rectangle.ins[len(Rectangle.ins)-1].color, Rectangle.ins[len(Rectangle.ins)-1].contrast, brightness)
        elif a==9:
            if len(Rectangle.ins)==0:
                print("There is no object")
            else:
                print("Brightness of last one:",Rectangle.ins[len(Rectangle.ins)-1].brightness)
        elif a==10:
            if len(Rectangle.ins)==0:
                print("There is no object")
            else:
                while(1):
                    try:
                        width=float(input("Enter new width ="))
                        heigh=float(input("Enter new heigh ="))
                        if (width<=0)or(heigh<=0):
                            raise Exception
                        break
                    except Exception:
                        print("Wrong data of variable(s)")
                Rectangle.ins[len(Rectangle.ins)-1].change_size(width,heigh)
        elif a==11:
            if len(Rectangle.ins)==0:
                print("There is no object")
            else:
                print("Width of last one:",Rectangle.ins[len(Rectangle.ins)-1].width)
                print("Heigh of last one:",Rectangle.ins[len(Rectangle.ins)-1].heigh)
        elif a==12:
            if len(Rectangle.ins)==0:
                print("There is no object")
            else:
                Rectangle.ins[len(Rectangle.ins)-1].moving()  
        else:
            break

while(True):
    print("Choose class:","1 - TShape", "2 - Pixel", "3 - Circle", "4 - Square", "5 - Rectangle")
    try:
        a=int(input())
        if (a<1)or(a>5):
            raise Exception
    except Exception:
        print("Choose from list, please")
        a=-1
    if a==1:
        TShapef()
    elif a==2:
        Pixelf()
    elif a==3:
        Circlef()
    elif a==4:
        Squaref()
    elif a==5:
        Rectanglef()



