windowHight = 500
windowWidth = 500

class LimitError(Exception):
    pass

class TLocation(object):
    instances = []

    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        cls.instances.append(instance)
        return instance

    def __del__(self):
        self.instances.remove(self)

    def __init__(self, x=1, y=1):
        try:
            x = int(x)
            if x>0 and x<=windowWidth:
                self.x = x
            else:
                raise ValueError
        except ValueError:
            print('unable to set horisontal coordinate {}; was set to default setting instead'.format(x))
            self.x = 1
        try:
            y = int(y)
            if y>0 and y<=windowHight:
                self.y = y
            else:
                raise ValueError
        except ValueError:
            print('unable to set vertical coordinate {}; was set to default setting instead'.format(y))
            self.y = 1

    def set_location(self, x, y):
        try:
            x = int(x)
            if x>0 and x<=windowWidth:
                self.x = x
            else:
                raise ValueError
        except ValueError:
            print('unable to set horisontal coordinate {}'.format(x))
        try:
            y = int(y)
            if y>0 and y<=windowHight:
                self.y = y
            else:
                raise ValueError
        except ValueError:
            print('unable to set vertical coordinate {}'.format(y))

    def get_location(self):
        return [self.x, self.y]

class TPoint(TLocation):
    instances = []
    limit = 40
    availableColours = ['none', 'black', 'white', 'green', 'red', 'blue']

    def __new__(cls, *args, **kwargs):
        try:
            if len(cls.instances) >= cls.limit:
                raise LimitError    
            instance = object.__new__(cls)
            cls.instances.append(instance)
            return instance
        except LimitError:
            print('unable to create; limit of objects created exceed for this type')

    def __init__(self, x=1, y=1, colour='none'):
        try:
            TLocation.__init__(self, x, y)
            colour = str(colour)
            if self.availableColours.count(colour)!=0:
                self.colour = colour
            else:
                raise ValueError
        except ValueError:
            print('unable to set colour {}'.format(colour))
            self.colour = 'none'
            
    def set_colour(self, colour):
        try:
            colour = str(colour)
            if self.availableColours.count(colour)!=0:
                self.colour = colour
            else:
                raise ValueError
        except ValueError:
            print('unable to set colour {}'.format(colour))

    def move(self, mx, my):
        try:
            mx = int(mx)
            my = int(my)
            if self.x+mx>0 and self.x+mx<=windowWidth and self.y+my>0 and self.y+my<=windowHight:
                self.x += mx
                self.y += my
            else:
                raise ValueError
        except ValueError:
            print('unable to move vertically by {} and horizontally by {}'.format(mx, my))

    def get_colour(self):
        return self.colour

class TEllipse(TPoint):
    instances = []

    def __init__(self, x=1, y=1, colours=['none', 'none'], width=1, hight=1):
        TPoint.__init__(self, x, y, colours[0])
        try:
            colourAddition = str(colours[1])
            if self.availableColours.count(colourAddition)!=0:
                self.colourAddition = colourAddition
            else:
                raise ValueError
        except ValueError:
            print('unable to set additional colour {}'.format(colourAddition))
            self.colourAddition = 'none'
        except IndexError:
            print('no additional colour is given')
        try:
            width = int(width)
            if width>0:
                self.width = width
            else:
                raise ValueError
        except ValueError:
            print('unable to set width of {}; was set to default setting instead'.format(width))
            self.width = 1
        if self.width%2==0:
            self.width -= 1
            print('width was even, redused by 1 to be centred properly')
        try:
            hight = int(hight)
            if hight>0:
                self.hight = hight
            else:
                raise ValueError
        except ValueError:
            print('unable to set hight of {}; was set to default setting instead'.format(hight))
            self.hight = 1
        if self.hight%2==0:
            self.hight -= 1
            print('hight was even, redused by 1 to be centred properly')

    def set_size(self, width, hight):
        try:
            width = int(width)
            if width>0:
                self.width = width
            else:
                raise ValueError
        except ValueError:
            print('unable to set width of {}'.format(width))
        if self.width%2==0:
            self.width -= 1
            print('width was even, redused by 1 to be centred properly')
        try:
            hight = int(hight)
            if hight>0:
                self.hight = hight
            else:
                raise ValueError
        except ValueError:
            print('unable to set hight of {}'.format(hight))
        if self.hight%2==0:
            self.hight -= 1
            print('hight was even, redused by 1 to be centred properly')

    def get_size(self):
        return [self.width, self.hight]

    def set_colour(self, colours):
        try:
            colour = str(colours[0])
            if self.availableColours.count(colour)!=0:
                self.colour = colour
            else:
                raise ValueError
        except ValueError:
            print('unable to set colour {}'.format(colour))
        try:
            colour = str(colours[1])
            if self.availableColours.count(colour)!=0:
                self.colourAddition = colour
            else:
                raise ValueError
        except ValueError:
            print('unable to set colour {}'.format(colour))
        except IndexError:
            print('no colour additional colour is given'.format(colour))

    def get_colour(self):
        return [self.colour, self.colourAddition]

class TKrug(TEllipse):
    instances = []

    def __init__(self, x=1, y=1, colour='none', radius=1, width=1, hight=1):
        TEllipse.__init__(self, x, y, [colour], width, hight)
        try:
            radius = int(radius)
            if radius>0:
                self.radius = radius
            else:
                raise ValueError
        except ValueError:
            print('unable to set radius of {}; was set to default setting instead'.format(radius))
            self.radius = 1

    def set_radius(self, radius):
        try:
            radius = int(radius)
            if radius>0:
                self.radius = radius
                TEllipse.set_size(self, radius*2, radius*2)
            else:
                raise ValueError
        except ValueError:
            print('unable to set radius of {}'.format(radius))

    def get_radius(self):
        return self.radius

    def set_colour(self, colour):
        TPoint.set_colour(self, colour)

    def get_colour(self):
        return self.colour

    def move(self, mx, my):
        try:
            mx = int(mx)
            my = int(my)
            if mx<0:
                self.x = 0
            elif mx>=0:
                self.x = windowWidth
            if my<0:
                self.y = 0
            elif my>=0:
                self.y = windowHight
            else:
                raise ValueError
        except ValueError:
            print('unable to move vertically by {} and horizontally by {}'.format(mx, my))

    def set_size(self, width, hight):
        TEllipse.set_size(self, width, hight)
        if self.width != self.radius*2-1:
            self.radius = int(self.width/2)+1
            self.hight = self.width
        elif self.hight != self.radius*2-1:
            self.radius = int(self.hight/2)+1
            self.width = self.hight

class TPie(TKrug):
    instances = []

    def __init__(self, x=1, y=1, colour='none', radius=1, width=1, hight=1, startDegree=0, extentDegree=0):
        TKrug.__init__(self, x, y, colour, radius)
        try:
            startDegree = int(startDegree)
            if startDegree>=0 and startDegree<360:
                self.startDegree = startDegree
            else:
                raise ValueError
        except ValueError:
            print('unable to set start degree of pie {}; was set to default setting instead'.format(startDegree))
        try:
            extentDegree = int(extentDegree)
            if abs(extentDegree)<=360:
                self.extentDegree = extentDegree
            else:
                raise ValueError
        except ValueError:
            print('unable to set extent degree of pie to {} from start degree; was set to default setting instead'.format(startDegree))

    def set_degrees(self, startDegree, extentDegree):
        try:
            startDegree = int(startDegree)
            if startDegree>=0 and startDegree<360:
                self.startDegree = startDegree
            else:
                raise ValueError
        except ValueError:
            print('unable to set start degree of pie {}'.format(startDegree))
        try:
            extentDegree = int(extentDegree)
            if abs(extentDegree)<=360:
                self.extentDegree = extentDegree
            else:
                raise ValueError
        except ValueError:
            print('unable to set extent degree of pie to {} from start degree'.format(startDegree))

    def get_degrees(self):
        return [self.startDegree, self.extentDegree]
